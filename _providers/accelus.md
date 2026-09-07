---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accelus-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: Accelus Inc. divested its whole product line — Remi robotic navigation to Alphatec in April 2023, the FlareHawk/Toro/LineSider implants to Highridge Medical in September 2025 — and its only host accelusinc.com is now a suspended cPanel account that 302s every path, including the root and a negative-control path, to an "Account Suspended" page behind a TLS certificate that expired 2026-05-13.
  evidence:
  - status: 302
    url: https://accelusinc.com/
  - status: 200
    url: https://accelusinc.com/cgi-sys/suspendedpage.cgi
  - status: 302
    url: https://accelusinc.com/openapi.json
  - status: 302
    url: https://accelusinc.com/.well-known/agent-card.json
  - status: 302
    url: https://accelusinc.com/.well-known/accelus-negative-control-7f3ab91c.json
  - status: 200
    url: https://equityzen.com/company/accelus/
  reason: defunct
  state: none
created: '2026-09-06'
description: Accelus was a Palm Beach Gardens, Florida medical device company formed in 2021 by the combination of Integrity Implants and Fusion Robotics, built around an "Adaptive Geometry" expandable-implant platform for minimally invasive spine surgery. Its products were the FlareHawk and Toro expandable interbody fusion systems for transforaminal, posterior and lateral lumbar interbody fusion, the LineSider minimally invasive pedicle screw system, and the Remi Robotic Navigation System, a table-mounted intra-operative navigation and robotics platform that guided instrumentation from 2D fluoroscopic or 3D imaging. The company raised roughly $32M from investors including Concord Health Partners, Symbiotic Capital, Eastward Capital Partners and Trog Hawley Capital. It sold the Remi robotic navigation assets to Alphatec Holdings for $55M in April 2023 and its remaining implant products and intellectual property — FlareHawk, Toro and LineSider — to Highridge Medical on 2 September 2025. Accelus
  sold surgical hardware and single-use implants to hospitals and surgeons, never operated a developer program, and published no public API, SDK, webhook surface or machine-readable specification. Its only host, the WordPress marketing site accelusinc.com, is now a suspended cPanel hosting account that returns an "Account Suspended" page on every path behind a TLS certificate that expired on 2026-05-13, and no accelusinc.com subdomain resolves. This profile is retained as a historical record; there is no API surface to enrich.
image: https://web.archive.org/web/20241002124548id_/https://accelusinc.com/wp-content/uploads/2021/07/accelus-logo_4c.png
layout: provider
modified: '2026-09-06'
name: Accelus
nav: Providers
network: true
overview: Accelus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Technology, Healthcare, and Spine Surgery.
random_paper: 1
security:
- kind: domain-security
  name: Accelus Domain Security
  slug: accelus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: accelus
tags:
- Company
- Medical Devices
- Medical Technology
- Healthcare
- Spine Surgery
- Surgical Robotics
- Implants
- Defunct
---
