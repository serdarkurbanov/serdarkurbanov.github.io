---
title: Documentation As Code With DacDoc
author: Serdar Kurbanov
date: 2019-10-01 20:55:00 -0500
categories: [Blogging, Technical]
tags: [dacdoc, documentation, programming]
image: /assets/img/sample/2019-10-01-dacdoc-intro/dacdoc_img_1.jpeg
---

## Technical documentation goes wrong
Nearly every project I was working on had problems with a technical documentation (unless a project didn't have it in the first place). It always starts clear and nice and then with the growth of a project it becomes a mess.

There are few typical flaws in the documentation that make it bad:
* *lack of documentation*. Making documentation is often a secondary priority. Sad but true.
* *outdated documentation*. Most often this is ghost links - someone had put down a list of resources and it got outdated.
* *duplicate documentation*. This usually happens when documentation is already quite big and no one is sure if it's up-to-date. Then instead of rewriting it users put additional page of documentation that contains some new information and also duplicates some pieces of already existing documents.

What would help keeping documentation alive is introducing *testable fragments* and providing a way to let reader know if certain pieces of a documentation are still valid (and if not - when it got changed and who changed it). Testable fragments can be project-specific, one of the most evident cases is checking ghost links, but generally speaking would be better to provide a way to generate custom checks around testable fragments. Examples can be checking DB connection, checking sequence of bash commands, checking list of users etc.

Components that can be used to implement this idea are:
* repo
* general purpose language to implement custom checks
* a way to compile raw documentation into tested version

I used git, java and maven to build an open source maven plugin that takes markdown files, searches for testable fragments, checks them for validity and produces the compiled version of a documentation where testable fragments are provided with valid/invalid indicators.
![links checked with dacdoc-maven-plugin](/assets/img/sample/2019-10-01-dacdoc-intro/dacdoc_img_2.png){: width="650" class="normal"}
_links checked with dacdoc-maven-plugin_

The name of the maven plugin - dacdoc - refers to documentation-as-code approach. You can find the documentation for the project here. There you can also find the example page that is built using same plugin with some checked statements.
Prerequisites
To create documentation and compile it with dacdoc-maven-plugin you'll need some things installed on your machine:
* java (1.8+)
* maven (I used version 3.3.9)
* git (I used version 2.7.4)

## Testable fragments
DacDoc plugin reads through markdown files and looks for testable fragments, then checks them. To make a piece of documentation testable and let dacdoc-maven-plugin recognize it one should surround it with DACDOC keyword and exclamation signs. For example, this is how a link to Medium will look like if turned into a testable fragment.
```md
!DACDOC{[medium](https://www.medium.com)}!
```

For custom checks test id should be given as well:
```md
!DACDOC{my custom testable fragment}(test=myCustomCheck)!
```

After compilation dacdoc will remove DACDOC keyword, leave the fragment intact and add validity indicator. So this fragment above will turn into something like this:
```md
![...](dacdoc-resources/circle-red-12px.png) my custom testable fragment
```

## Documentation as code
dacdoc-maven-plugin treats your documentation folder as maven project so you'll need `pom.xml` in the root of the documentation project to make it work. The essential part of pom file is reference to plugin, so you can run compile command. The best example would be pom file that is used in dacdoc project itself - you can find it here.

Compiling your documentation is done with compile comand. It transforms your markdown files, supplementing testable fragments with validity indicators.
```shell
mvn com.github.flussig:dacdoc-maven-plugin:compile
```

To fully utilize the capabilities of dacdoc-maven-plugin your documentation should be kept in git repo. Git blame is then used to get the history of changes of a given markdown file. When you hover over a validity indicator it will show a history info associated with this fragment.
![dacdoc-maven-plugin attaches history for a given tested link using git blame](/assets/img/sample/2019-10-01-dacdoc-intro/dacdoc_img_3.png){: width="650" class="normal"}
_dacdoc-maven-plugin attaches history for a given tested link using git blame_

Custom checks are defined in classes that inherit from base `Check` or `SingleExecutionCheck` class defined in dacdoc-check module. Classes should be placed where maven expects them: in `src/main/java` or `src/test/java` directories. Essential part is that the class must override performCheck methods and use constructor that takes argument and reference to the documentation file.

<script src="https://gist.github.com/serdarkurbanov/ff9add6228c6e7dc43cbefedd5ef430b.js"></script>

user-defined check for dacdoc-maven-plugin ^^

Example of such a user-defined check can be found in the code for github pages documentation of dacdoc project (here).

## Continuous delivery of documentation
When using DacDoc it's convenient to keep raw version of documentation in one branch (development) and compiled version in another (release). Then it's possible to build a CI/CD pipeline to compile and push documentation from development to release.

For example, here's the Travis CI file from gh-pages-development branch of dacdoc project (it plays the role of development branch for github pages documentation whereas gh-pages branch plays the role of release branch). This CI job builds documentation for the project nightly and every time new commit is pushed to the gh-pages-development branch.

This is what happens in CI step by step:
1. checkout documentation release branch and pull from origin
```console
$ git checkout -b gh-pages; git pull;
```
2. replace all content with files from documentation development branch
```console
$ git reset --hard gh-pages-development;
```
3. compile documentation project (necessary step if there are custom checks)
```console
$ mvn clean compile;
```
4. run dacdoc-maven-plugin and perform all the checks
```console
$ mvn com.github.flussig:dacdoc-maven-plugin:compile;
```
5. commit changes to release branch
```console
$ git add .; git commit -m "release documentation";
```
6. push to release origin
```console
$ git push --force gh-pages;
```

## Pros/Cons
Some of the benefits of DacDoc approach to documentation are:
* proper versioning and collaboration via git
* ability to checkout documentation from git and read it offline
testable fragments that will tell user if given piece is still valid and who changed it

Having said this, there are some difficulties extending this approach outside of domain of technical documentation. First, business-facing documentation is often too high-level to break it into testable pieces. Second, DacDoc approach relies on some technical solutions that are hard to grasp for non-developers (java, maven and git).

## Contribute to the project
The project is a minimal viable product now and there are a lot of features that can be added to the project to make it better. For example, dacdoc has only maven plugin now, but many use gradle. Also, the idea may be extended to outside of java world. Would be cool to add actions on documentation builds - for example notify the user if he/she was the last user to modify a testable fragment that started failing.

Contributions are very welcome (along with thoughts, comments and criticism of the idea)! Here's the github repo for dacdoc project for anyone interested.

## Resources
[dacdoc github repo](https://github.com/flussig/dacdoc)

[dacdoc github pages](https://flussig.github.io/dacdoc/#/)

[dacdoc example documentation page](https://flussig.github.io/dacdoc/#/docs/example)
