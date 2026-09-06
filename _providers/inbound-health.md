---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inbound-health-domain-security.yml
coverage:
  checked: '2026-08-23'
  detail: Inbound Health ceased operations in December 2025 and MedArrive bought its care-navigation technology assets in March 2026; inboundhealth.com now answers Cloudflare HTTP 526 on every HTTPS path because its origin is gone, plain HTTP returns an identical "Site is not available" 404 page on every path including a nonsense control, none of the api/docs/developer/app/portal/status subdomains resolve in DNS, and the InboundHealth GitHub organization has zero public repositories, so there is no surface left to profile.
  evidence:
  - status: 526
    url: https://inboundhealth.com/
  - status: 526
    url: https://inboundhealth.com/openapi.json
  - status: 526
    url: https://inboundhealth.com/.well-known/agent-card.json
  - status: 526
    url: https://inboundhealth.com/llms.txt
  - status: 404
    url: http://inboundhealth.com/zzz-does-not-exist-9f3a
  - status: 200
    url: https://api.github.com/users/InboundHealth
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Inbound Health was a Minneapolis, Minnesota company that enabled health systems and health plans to deliver hospital-level and skilled-nursing-level care in patients'' homes. It was spun out of Allina Health''s own Hospital-at-Home and SNF-at-Home programs in October 2022 with $20 million from Flare Capital Partners, and was led by co-founder and chief executive Dave Kerwar, previously chief product officer at Mount Sinai Health System, with Dr. Chi Huang as chief medical officer and Dave Zimmerman as chief operating officer. The company raised a $30 million Series B in September 2023 led by HealthQuest Capital, and in February 2024 released Inbound InHome, a proprietary patient-management and analytics platform for advanced care in the home: AI/ML-assisted identification and eligibility screening of candidate patients, device-agnostic biometric monitoring across devices, wearables and in-home sensors, a virtual care module carrying real-time video, audio, text and alerting
  between patient and care team, a workflow application automating logistics across the care episode, supply-chain management, and integration points into multiple EMRs. Inbound Health ceased operations in December 2025 after regulatory uncertainty over the federal Acute Hospital Care at Home (AHCAH) waiver stalled its next financing round; MedArrive acquired its AI-backed care-navigation technology assets in March 2026. Inbound InHome was sold only under signed health-system and health-plan agreements, and no public developer portal, API reference, SDK, or machine-readable specification (OpenAPI, AsyncAPI, GraphQL SDL, MCP manifest or A2A agent card) was ever published on an Inbound Health host. Both inboundhealth.com and www.inboundhealth.com now fail at the origin behind Cloudflare (HTTP 526) and every api/docs/developer/app/portal/status subdomain has been removed from DNS, so there is no live API surface to catalog. This profile is retained as a historical record.'
layout: provider
modified: '2026-08-23'
name: Inbound Health
nav: Providers
network: true
overview: Inbound Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Healthcare, Hospital at Home, and Home Health.
random_paper: 19
security:
- kind: domain-security
  name: Inbound Health Domain Security
  slug: inbound-health-domain-security
  summary_line: TLSv1.3
slug: inbound-health
tags:
- Company
- Defunct
- Healthcare
- Hospital at Home
- Home Health
- Remote Patient Monitoring
- Value-Based Care
- Care Coordination
- Health Systems
- Digital Health
---
