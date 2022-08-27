---
title: Data aggregation - types and pitfalls
author: Serdar Kurbanov
date: 2022-08-24 17:00:00 -0500
categories: [Blogging, Technical]
tags: [data, aggregation]
image: /assets/img/sample/2022-08-24-data-aggregators/escher-distorted.jpg
---

(Image: [link](https://www.sothebys.com/en/buy/auction/2019/prints-multiples-day-sale/m-c-escher-print-gallery-bklw-410))

## Data aggregators

Every now and then the big organization comes with the need of simplifying data fetch from multiple systems - hence building the data aggregator. Aggregation is such an attractive idea that sometimes it comes without a need - just because we, humans, love it. If we lived in the machine-dominated world, we'd probably not need any aggregation at all, or it would be built much differently. Here I'd like to describe few approaches to data aggregation and the elements of human nature that affect their designs.

This essay mostly applies to big organizations comprised of multiple subsystems - because I mostly dealt with this type of organizations. However, it will apply to smaller systems, difference will be that bigger systems would smoother out exceptions (for instance, a strong influence of individuals) while smaller will not.

Also, in this essay I deliberately don't specify the technology selected for data aggregation: data can be stored in various DBs, served through GraphQL or REST or gRPC. I'd like to concentrate on architectural/organizational challenges that comes with aggregation rather than details of the chosen technology.

## Types of data aggregation

First, the problem statement: imagine that your company has a number of systems that hold some specific data. You would like to build a way to fetch data from client applications (internal or external). Ideally you

There are a few types of aggregation that I know:
* *lump model* - stable state
* aggregation through references
* aggregation through routing
* aggregation through cache

(add note about not using app-facing backend as data aggregator for other apps)

# Lump model

The company may decide to not build data aggregators, and in theory the app interaction will look like this:
![no data aggregation and no lumps](/assets/img/sample/2022-08-24-data-aggregators/no-aggregation-init.png){: width="650" class="normal"}

This picture is however doesn't depict the ground (most stable) state of the system. In fact, the organization will require efforts to keep it like this. The true stable state will evolve from this system naturally: some teams will decide to build a cache, some others will introduce a small orchestration service that will be reused by some other apps thinking that this the real source of truth. Some decisions like this will be temporary, some will cement over time. In time the system will evolve into the lump model:
![no data aggregation and no lumps](/assets/img/sample/2022-08-24-data-aggregators/no-aggregation-lump.png){: width="650" class="normal"}

In fact, all the other types of aggregation also gravitate to the lump model as entropy of the system grows and the structure of the system erodes.

# Aggregation with references

# Aggregation with routing

# Aggregation with cache

## Summary

Apart from technical details of implementing aggregation service, the human nature adds 2 strong centers of gravity that will drive the design of components of a system:
* using the data
* storing the data

The designs then tend to keep the systems that face the final users (using the data) and systems that store the data. The intermediate layers tend to be very fluid. They can easily lack support and resources unless they're artificially reinforced by few levels of leadership. Keeping these layers stable isn't only a technical but also an organizational challenge.

Organizational challenge is hard to quantify: how much firmness do you add into your org so that it maintains the organizational structure and also that it doesn't become a dictatorship? Being a lead (architect, manager, director) requires hearing the feedback, placing the limits of pursuing certain goals and allowing certain level of chaos in your organization. Controlling this chaos and allowing different levels of it in different situations is essentially the art of leadership.

Another related piece of knowledge: the architectural choices that are based on conventions - like for instance a convention of what aggregation strategy to choose - will eventually dissolve (as I mentioned they need to be reinforced by few levels of leadership). Few things will make them more solid:
* technical frameworks - building a platform instead of a specific service
* wide adoption - keep aggregation layers close to where they are used