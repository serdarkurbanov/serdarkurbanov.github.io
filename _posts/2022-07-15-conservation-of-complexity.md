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

Does life of a team become easier with introducing the new framework or out of box solution? No! The experience in the field tells that the complexity that can be supported by a given team stays about same - hence the conservation of complexity.

The point of this post is to shift the focus: from thinking of burden removed by simplifications to thinking of what kind of complexity will fill the void created by taking another complexity out.

## Human factor

Working on an algorithm doesn't involve a lot of human problems. But making the organization comprised of software engineers follow the same goal and build coherent solutions to commonly understood problems is mainly about human interactions and less about technology.

The complexity that a given team of developers can maintain is about constant. The tricky part is that simply removing the complexity from a team doesn't leave it in the simplified state for long. The complexity void will be filled by people of that team - and it can be filled in random direction. This is why it's important to define the direction for the future development and maybe start building in this direction before the current burden is taken away.

Say we introduced a new out of box metrics solution that removes the burden of supporting custom metrics. The reduced complexity can be filled with adding a long needed feature or building dashboards based on new metrics. But without a well-defined priorities and development that started ahead it's likely to be filled randomly. The burden of custom metrics can easily be replaced by a burden of supporting custom dashboards. This is why as an architect that brought the said out of box solution, one also needs to outline the limits of using it.

That also says that as much as I'm inclined to build apps on a firm foundation of an underlying platform, some healthy amount of 'visionary' style development is necessary. It sets anchors/ideas that pull the team in the right direction when the complexity conservation law allows.
