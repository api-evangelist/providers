---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avago-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avagotech.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/broadcom/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avago-technologies-llms.txt
coverage:
  checked: '2026-09-13'
  detail: 'Avago Technologies Limited renamed itself Broadcom Limited on 1 February 2016 after acquiring Broadcom Corporation, so the brand has no surface of its own: every path on avagotech.com returns an HTTP 301 to broadcom.com, avago.com is a third-party domain-brokerage landing page, and no Avago GitHub organization, developer portal, package or machine-readable contract exists.'
  evidence:
  - status: 301
    url: https://www.avagotech.com/
  - status: 301
    url: https://www.avagotech.com/openapi.json
  - status: 301
    url: https://www.avagotech.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/avagotech
  - status: 200
    url: https://avago.com/
  reason: defunct
  state: none
created: '2026-09-13'
description: 'Avago Technologies Limited was the Singapore-headquartered semiconductor company spun out of Agilent Technologies'' semiconductor products group in 2005 that acquired Broadcom Corporation for $37 billion on February 1, 2016 and renamed itself Broadcom Limited, today Broadcom Inc. (NASDAQ: AVGO). Avago is therefore not a subsidiary of Broadcom but its legal predecessor and former corporate name. The brand is retired: every path on avagotech.com returns an HTTP 301 to broadcom.com, avago.com is a third-party domain-brokerage landing page rather than a company site, and no Avago-branded developer portal, documentation, OpenAPI, SDK, package or GitHub organization exists. API surfaces once associated with Avago product lines (LSI and Emulex storage controllers, fiber optics, RF) are published today by Broadcom and are profiled under the broadcom record.'
layout: provider
modified: '2026-09-13'
name: Avago Technologies
nav: Providers
network: true
overview: Avago Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Electronic Components, and Acquired.
random_paper: 7
security:
- kind: domain-security
  name: Avago Technologies Domain Security
  slug: avago-technologies-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: avago-technologies
tags:
- Company
- Semiconductors
- Hardware
- Electronic Components
- Acquired
- Legacy Brand
- Broadcom
website: https://www.avagotech.com/
---
