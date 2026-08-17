---
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: 'DESKi ships regulated end-user software, not a platform: HeartFocus is an FDA-cleared iPhone/iPad app whose only machine-facing interface is a DICOM push to a PACS the customer configures in-app, and the DICOM conformance statement that would describe it is available only by emailing support@deski.ai — /openapi.json, /graphql, /llms.txt and every /.well-known/* path return a real 404 on www.heartfocus.ai and deski.ai, api./developer./link.heartfocus.ai do not resolve in DNS, docs.heartfocus.ai is an S3 bucket returning 403 AccessDenied, and portal.heartfocus.ai is a licence-management SPA that answers 200 with the same 467-byte HTML shell for every path probed.'
  evidence:
  - status: 404
    url: https://www.heartfocus.ai/openapi.json
  - status: 404
    url: https://www.heartfocus.ai/graphql
  - status: 404
    url: https://www.heartfocus.ai/llms.txt
  - status: 404
    url: https://www.heartfocus.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.heartfocus.ai/.well-known/security.txt
  - status: 404
    url: https://deski.ai/.well-known/agent.json
  - status: 403
    url: https://docs.heartfocus.ai/
  - status: 200
    url: https://portal.heartfocus.ai/openapi.json
  - status: 200
    url: https://www.heartfocus.ai/security/cvd
  - status: 200
    url: https://www.heartfocus.ai/pricing
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'DESKi is a French medical-device software company founded in 2016 in Bordeaux by brothers Bertrand and Olivier Moal, trading publicly under its HeartFocus brand. Its flagship product, HeartFocus, is an FDA-cleared AI cardiac imaging app that runs on iPhone and iPad with Butterfly Network iQ+ and iQ3 handheld ultrasound probes, giving any healthcare professional real-time probe guidance, automatic diagnostic-quality clip recording and live view validation across the 10 standard transthoracic echocardiographic views (PLAX, PSAX-AV, PSAX-MV, PSAX-PM, A4C, A5C, A2C, A3C, SC-4C, SC-IVC). A second product, HeartFocus Link, adds the same AI guidance to existing cart-based ultrasound systems from GE HealthCare, Philips, Siemens Healthineers, Mindray, FUJIFILM Sonosite, Samsung and Canon over a plain HDMI capture path, for education and training only. DESKi holds two FDA 510(k) clearances (K242807, 2025-04-04; K260780, 2026-06-03, product code QJU) and publishes a Coordinated Vulnerability
  Disclosure process, a HIPAA & HBNR applicability statement, per-probe list pricing and dated electronic instructions for use. Its only machine-facing integration surface is DICOM: exams are transferred from the mobile app to a customer-configured PACS server (server and client AE titles, host, port, optional TLS), and the DICOM conformance statement and CycloneDX SBOM are available only by emailing support. DESKi publishes no public REST or GraphQL API, no OpenAPI or AsyncAPI specification, no SDK, no CLI, no MCP server and no developer portal; portal.heartfocus.ai is a customer licence-management application, not a developer surface.'
image: https://cdn.prod.website-files.com/6634a89a6fab56ada55e9d51/67b5d8e31ab3b8fe2d8e6bd2_DESKi%20Logo.png
layout: provider
modified: '2026-08-17'
name: DESKi
nav: Providers
network: true
random_paper: 81
slug: deski
tags:
- Company
- Healthtech
- Medical Imaging
- Cardiology
- Ultrasound
- Point-of-Care Ultrasound
- Artificial Intelligence
- Medical Device
- DICOM
- France
---
