---
title: Data aggregation: types and pitfalls
author: Serdar Kurbanov
date: 2022-08-24 17:00:00 -0500
categories: [Blogging, Technical]
tags: [data, aggregation]
image: /assets/img/sample/2022-08-24-data-aggregators/smth.jpg
---

## Data aggregators

Every now and then the big organization comes with the need of simplifying data fetch from multiple systems - hence building the data aggregator. Aggregation is such an attractive idea that sometimes it comes without a need - just because we, humans, love it. If we lived in the machine-dominated world, we'd probably not need any aggregation at all, or it would be built much differently. Here I'd like to describe few approaches to data aggregation and the elements of human nature that affect their designs.

This essay mostly applies to big organizations comprised of multiple subsystems - because I mostly dealt with this type of organizations. However, it will apply to smaller system, difference will be that bigger systems would smoother out exceptions (for instance, a strong influence of individual architects) while smaller will not.
