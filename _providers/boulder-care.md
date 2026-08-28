---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boulder-care-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boulder-care-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.boulder.care/
- group: company
  title: ''
  type: About
  url: https://www.boulder.care/about
- group: company
  title: ''
  type: Blog
  url: https://www.boulder.care/blog
- group: operate
  title: ''
  type: Support
  url: https://www.boulder.care/support
- group: operate
  title: ''
  type: Contact
  url: https://www.boulder.care/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.boulder.care/faqs
- group: start
  title: ''
  type: SignUp
  url: https://www.boulder.care/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.boulder.care/self-pay
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boulder.care/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boulder.care/legal/platform-privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.boulder.care/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bouldercare
- group: company
  title: ''
  type: Partners
  url: https://www.boulder.care/partners
- group: company
  title: ''
  type: Careers
  url: https://www.boulder.care/careers
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.boulder.care/services
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boulder
- group: other
  title: ''
  type: MobileApp
  url: https://apps.apple.com/us/app/boulder-care/id1437606990
- group: other
  title: ''
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=bouldercare.patient
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/boulder-care_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boulder-care-llms.txt
coverage:
  checked: '2026-08-08'
  detail: Boulder Care ships software only as an end-user patient app — its 156-URL sitemap contains no developer, docs, API or integration page, and the only machine API on any host is an undocumented Apollo GraphQL endpoint at the root of api.boulder.care that serves the mobile app and refuses introspection with INTROSPECTION_DISABLED.
  evidence:
  - status: 404
    url: https://www.boulder.care/developers
  - status: 404
    url: https://www.boulder.care/openapi.json
  - status: 404
    url: https://www.boulder.care/llms.txt
  - status: 404
    url: https://www.boulder.care/.well-known/security.txt
  - status: 400
    url: https://api.boulder.care/
  - status: 200
    url: https://api.boulder.care/health
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: 'Boulder Care is a Portland, Oregon telehealth provider founded in 2017 by Stephanie Strong that delivers evidence-based outpatient treatment for opioid and alcohol use disorder entirely through a mobile app. Participants connect to a collaborative care team — addiction medicine clinicians, peer recovery specialists and care coordinators — over secure video and messaging, and are prescribed medications for addiction treatment including buprenorphine/naloxone (Suboxone), naltrexone (Revia, Vivitrol) and acamprosate (Campral). The company focuses on Medicaid beneficiaries and other historically underserved populations, contracts with health plans, health systems, employers and correctional and jail-based referral partners, and has served more than 12,000 participants across states including Oregon, Washington, Colorado, North Carolina, New Mexico, Ohio and Michigan. Boulder Care raised a $35M Series C in 2024 led by Advance Venture Partners. It ships software only as an end-user
  patient product: there is no developer portal, no published API documentation, no SDK and no machine-readable specification anywhere on its public surface.'
image: https://cdn.prod.website-files.com/61a529f90d9568244b6f6716/621d5fdca5956ee9ec3de8c2_logo_primary_light.svg
layout: provider
modified: '2026-08-08'
name: Boulder Care
nav: Providers
network: true
overview: 'Boulder Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Behavioral Health, and Addiction Treatment.


  Boulder Care''s developer surface includes engineering blog, support, FAQ, signup flow, pricing, legal docs, and 16 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 20.5
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 20.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Boulder Care Domain Security
  slug: boulder-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boulder-care
tags:
- Company
- Healthcare
- Telehealth
- Behavioral Health
- Addiction Treatment
- Substance Use Disorder
- Digital Health
- Medicaid
- Virtual Care
- Mobile Health
website: https://www.boulder.care/
---
