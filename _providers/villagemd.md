---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.villagemd.com/
- group: company
  title: ''
  type: About
  url: https://www.villagemd.com/who-we-are
- group: other
  title: ''
  type: Services
  url: https://www.villagemedical.com/our-services
- group: start
  title: ''
  type: PatientPortal
  url: https://www.villagemedical.com/patient-portal
- group: operate
  title: ''
  type: Contact
  url: https://www.villagemd.com/contact-us
- group: company
  title: ''
  type: Careers
  url: https://www.villagemd.com/careers
- group: company
  title: ''
  type: Blog
  url: https://www.villagemedical.com/journey-to-well
- group: company
  title: ''
  type: Press
  url: https://www.villagemd.com/press-releases
- group: company
  title: ''
  type: News
  url: https://www.villagemd.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VillageMD
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.villagemedical.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.villagemedical.com/privacy-policy
- group: commercial
  title: ''
  type: LegalAndPrivacy
  url: https://www.villagemd.com/legal-and-privacy
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.villagemd.com/code-of-conduct
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/villagemd
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/villagemd_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/villagemd-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/villagemd-llms.txt
coverage:
  checked: '2026-08-05'
  detail: VillageMD is a clinic operator, not a software vendor — villagemd.com and villagemedical.com are HubSpot marketing sites whose sitemaps contain no developer, API, FHIR or interoperability page, no api/developer/docs/fhir subdomain resolves, and patient record access is delivered by its EHR vendor athenahealth, whose certified FHIR R4 API is athenahealth's to publish rather than VillageMD's.
  evidence:
  - status: 404
    url: https://www.villagemd.com/llms.txt
  - status: 404
    url: https://www.villagemd.com/.well-known/security.txt
  - status: 404
    url: https://www.villagemd.com/openapi.json
  - status: 200
    url: https://www.villagemedical.com/sitemap.xml
  - status: 200
    url: https://care.villagemedical.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/VillageMD
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'VillageMD is a Chicago-based, value-based primary care organization that operates and supports physician practices across the United States through its Village Medical, Village Medical at Home, Summit Health, CityMD and Starling Physicians operating companies, serving millions of patients across primary care, multispecialty and urgent care. It runs clinics — free-standing practices, in-Walgreens practices, home-based care and virtual visits — rather than selling software, and its clinical record and patient-facing digital surface run on athenahealth: patient portals are hosted at practice-specific athenahealth portal subdomains and the Village Medical mobile app is the athenaPatient experience. VillageMD publishes no developer portal, no API documentation, no machine-readable specification and no SDK; the only public machine-readable interfaces touching its patients are athenahealth''s certified FHIR R4 APIs, which are operated and documented by athenahealth, not by VillageMD.
  Since Sycamore Partners took Walgreens Boots Alliance private in August 2025, VillageMD has operated as a standalone company in that portfolio.'
image: https://www.villagemd.com/hs-fs/hubfs/villagemd-logo-1.png
layout: provider
modified: '2026-08-05'
name: VillageMD
nav: Providers
network: true
overview: 'VillageMD is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, Value-Based Care, and Medical Practices.


  VillageMD''s developer surface includes engineering blog, product news, and 16 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 11.7
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Villagemd Domain Security
  slug: villagemd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: villagemd
tags:
- Company
- Healthcare
- Primary Care
- Value-Based Care
- Medical Practices
- Urgent Care
- Telehealth
- Patient Care
- Clinics
website: https://www.villagemd.com/
---
