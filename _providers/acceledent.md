---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-06'
  detail: OrthoAccel Technologies built AcceleDent as a physical FDA-cleared Class II orthodontic device and never ran a developer program; the company is now defunct, orthoaccel.com no longer resolves at all, and acceledent.com was re-registered in August 2022 as a GoDaddy aftermarket "for sale" listing whose parking system returns the same 114-byte HTML stub with HTTP 200 for every path probed, including /openapi.json and every /.well-known/ path.
  evidence:
  - status: 200
    url: https://acceledent.com/
  - status: 403
    url: https://acceledent.com/lander
  - status: 200
    url: https://acceledent.com/openapi.json
  - status: 200
    url: https://acceledent.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/orthoaccel
  - status: 403
    url: https://forgeglobal.com/acceledent_stock/
  reason: defunct
  state: none
created: '2026-09-06'
description: 'AcceleDent was the flagship product of OrthoAccel Technologies, Inc., a privately held medical-device company founded in 2007 and headquartered in Bellaire, Texas, outside Houston. AcceleDent is an FDA-cleared Class II device built around the company''s patented SoftPulse Technology: a hands-free mouthpiece and activator that a patient bit down on for about twenty minutes a day, delivering gentle micropulses intended to speed bone remodeling during orthodontic treatment and reduce the discomfort of braces and clear aligners. The line ran through three generations — the original AcceleDent, AcceleDent Aura in 2013, and AcceleDent Optima, cleared by the FDA in 2017 — sold to orthodontists and dentists rather than direct to consumers, with an e-commerce ordering site at shop.acceledent.com for practices. The company raised roughly $63.1M across sixteen rounds, the last a Series C in January 2017, and a later debt-and-equity financing led by S3 Ventures. It was a physical medical-device
  business, not a software business: OrthoAccel never operated a developer program, never published an API, SDK, webhook surface or machine-readable specification of any kind, and shipped no client libraries to any package registry. OrthoAccel is now reported defunct — orthoaccel.com no longer resolves, and acceledent.com was re-registered on 2022-08-30 and today sits on Afternic name servers as a GoDaddy aftermarket "for sale" listing whose parking system answers HTTP 200 with an identical 114-byte HTML stub on every path, including every /.well-known/ and spec path. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-06'
name: AcceleDent
nav: Providers
network: true
overview: AcceleDent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Medical Device, Dental, and Orthodontics.
random_paper: 3
slug: acceledent
tags:
- Company
- Defunct
- Medical Device
- Dental
- Orthodontics
- Healthcare
- Hardware
- Consumer Health
---
