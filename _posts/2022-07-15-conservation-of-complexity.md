---
title: The conservation of complexity in software development teams
author: Serdar Kurbanov
date: 2022-07-15 17:00:00 -0500
categories: [Blogging, Technical]
tags: [complexity]
image: /assets/img/sample/2022-07-15-conservation-of-complexity/escher-in-his-minds-eye.jpg
---

## Simplifying complex systems

Often when considering using a new framework or building a new system we think first and foremost about the simplification it will bring. Everyone secretly dreams of having a perfectly working software that will be easily configurable, easily extendable and will never crash.

It will be so much easier to build new endpoints with Springboot. It will be a breeze to build new metrics with Grafana.

Some time after the new system is introduced we find ourselves supporting more infrastructure, building complicated configuration and opening the whole new dimension of complexity we didn't know existed.

Does the life become easier with introducing new technology? No! The experience in the field tells that the complexity that can be supported by a given team stays about same - hence the conservation of complexity.

The point of this post is to shift the focus: from thinking of burden removed by simplifications to thinking of what kind of complexity will fill the void created by taking another complexity out.

## Human factor

Working on an algorithm doesn't involve a lot of human problems. But making the organization comprised of software engineers follow the same goal and build coherent solutions to commonly understood problems is mainly about human interactions and less about technology.

I mentioned that the complexity that a given team of developers can maintain is about constant. The tricky part is that simply removing the complexity from a team can result in people of that team filling the void with random additional complexity. Say we introduced a new out of box logging solution that removes the burden of supporting custom logging. 
