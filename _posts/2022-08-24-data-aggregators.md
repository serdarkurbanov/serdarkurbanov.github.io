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

This essay mostly applies to big organizations comprised of multiple subsystems - because I mostly dealt with this type of organizations. However, it will apply to smaller systems, difference will be that bigger systems would smoother out exceptions (for instance, a strong influence of individuals) while smaller will not.

Also, in this essay I deliberately don't specify the technology selected for data aggregation: data can be stored in various DBs, served through GraphQL or REST or gRPC. I'd like to concentrate on architectural/organizational challenges that comes with aggregation rather than details of the chosen technology.

## Types of data aggregation

First, the problem statement: imagine that your company has a number of system that hold some specific data. You would like to build an effective way to fetch data from client applications (internal or external).

There are a few types of aggregation that I know:
* no aggregation
* aggregation with references
* aggregation with routing
* aggregation with cache

(add note about not using app-facing backend as data aggregator for other apps)

# No aggregation

# Aggregation with references

# Aggregation with routing

# Aggregation with cache

## Summary

Apart from technical details of implementing aggregation service, the human nature adds 2 strong centers of gravity that will drive the design of components of a system:
* using the data
* storing the data

The designs then tend to keep the systems that face the final users (using the data) and systems that store the data. The intermediate layers tend to be very fluid. They can easily lack support and resources unless they're artificially reinforced by few levels of leadership. Keeping these layers stable isn't only a technical but also an organizational challenge.
