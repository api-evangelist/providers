---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-12'
  detail: 'AggreDyne sells a benchtop laser light scattering platelet aggregometer and its single-use cartridges — an FDA 510(k) class of physical in vitro diagnostic goods (K122162, K163274, K181777, all product code JOZ), not software — and there is no developer program, GitHub organization (github.com/aggredyne is a hard 404, and a GitHub code search for "aggredyne" returns zero repositories) or integration surface of any kind attached to it. The company surface could not be walked live either: the aggredyne.com hosting account is SUSPENDED, so the origin answers every path on both aggredyne.com and www.aggredyne.com with an identical 7,768-byte cPanel "Account Suspended" page (plain HTTP 302s to /cgi-sys/suspendedpage.cgi), and its Let''s Encrypt certificate, CN=cpanel.aggredyne.com, expired on 2026-05-15. That catch-all makes the HTTP 200 on every REST, GraphQL, MCP, agent-card, llms.txt and /.well-known/ probe a false positive — a random control path returns byte-identical content
    — so all sixteen well-known probes are recorded as misses and no WellKnown, SecurityTxt or AgentCard pointer was wired. The api./app./portal./developer./cloud. subdomains resolve only to the same shared cPanel wildcard IP 162.253.33.192, not to distinct surfaces. The harvest lead''s original Website pointer, https://www.nasdaqprivatemarket.com/, was the secondary-market platform''s own home page rather than this company''s site and has been removed.'
  evidence:
  - status: 302
    url: http://www.aggredyne.com/
  - status: 200
    url: https://www.aggredyne.com/
  - status: 200
    url: https://www.aggredyne.com/this-path-does-not-exist-zzz9876
  - status: 200
    url: https://www.aggredyne.com/openapi.json
  - status: 200
    url: https://www.aggredyne.com/swagger.json
  - status: 200
    url: https://www.aggredyne.com/graphql
  - status: 200
    url: https://www.aggredyne.com/llms.txt
  - status: 200
    url: https://www.aggredyne.com/.well-known/agent-card.json
  - status: 200
    url: https://aggredyne.com/.well-known/api-catalog
  - status: 200
    url: https://aggredyne.com/.well-known/security.txt
  - status: 404
    url: https://github.com/aggredyne
  - status: 200
    url: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K181777
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'AggreDyne, Inc. is a privately held Houston, Texas medical device and in vitro diagnostics manufacturer, founded in 2011 by Edward R. Teitel, MD, JD and Robert C. Hux, CPA, to commercialize the AggreGuide platelet function analyzer. Its flagship product, the AggreGuide A-100, is a benchtop laser light scattering aggregometer that measures platelet aggregation from a single-use disposable cartridge in under five minutes, assessing how well a patient is responding to antiplatelet therapy such as aspirin, clopidogrel, prasugrel and ticagrelor. The company holds three FDA 510(k) clearances under product code JOZ — K122162 (2013), K163274 for the A-100 AA Assay and Instrument (2017), and K181777 for the A-100 ADP assay cartridge (2019) — and its products are CE marked. It sells to hospital laboratories, physician office laboratories in cardiology, endocrinology, neurology and family practice, and regional reference laboratories. AggreDyne is a diagnostic instrument and consumable
  manufacturer rather than a software or platform business: it has never published a developer program, public API, SDK, or machine-readable API contract, and as of September 2026 its corporate website is offline behind a suspended hosting account.'
layout: provider
modified: '2026-09-12'
name: AggreDyne
nav: Providers
network: true
random_paper: 5
slug: aggredyne
tags:
- Company
- Medical Devices
- Diagnostics
- In Vitro Diagnostics
- Healthcare
- Hematology
- Platelet Function Testing
- Laboratory
- Manufacturing
---
