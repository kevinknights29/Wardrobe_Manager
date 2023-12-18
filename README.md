# Wardrobe_Manager

This project aims to create a webapp to keep track of your clothing usage.

## Topics

1. [Overview](#overview)
2. [Goals](#goals)
3. [Scope and Context](#scope-and-context)
4. [System Design](#system-design)
5. [Alternatives Considered](#alternatives-considered)
6. [Learning Logs](#learning-logs)
7. [Resources](#resources)

---

![image](https://github.com/kevinknights29/Wardrobe_Manager/assets/74464814/dc682d99-cab4-4668-9be5-de19b49af921)

## Overview

## Goals

## Scope and Context

## System Design

```mermaid
---
title: Home Page Flow
---
flowchart LR
    i([Take Item])
    t1[Take Picture of Item]
    t2[Classify Item]
    d1{Wore Item?}
    t3[Log Item Usgae]
    o([Submit Item])
    i --> t1
    t1 --> t2
    t2 --> d1
    d1 -- Yes --> t3
    d1 -- No --> o
    t3 --> o
```

```mermaid
---
title: Submission Flow
---
flowchart LR
    i([Recieve Data])
    d1{Is Complete?}
    t1[Transform Data]
    t2[Create DB Connection]
    d2{Succeeded?}
    e([Raise Error])
    o([Store Data in DB])
    i --> d1
    d1 -- Yes --> t1
    d1 -- No --> e
    t1 --> t2
    t2 --> d2
    d2 -- Yes --> o
    d2 -- No --> e
```

## Alternatives Considered

## Learning Logs

| Date | Learning |
|------|----------|
|      |          |

## Resources
