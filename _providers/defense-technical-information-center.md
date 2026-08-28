---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: 'Public-facing website of the Defense Technical Information Center describing DTIC services, products, and access programs. The site links to Discover, R&E Gateway, training, and registration but does '
  name: DTIC Website
  slug: defense-technical-information-center-website
- description: 'Search platform for DTIC''s collection of technical reports and other scientific and technical information assets. Discover offers faceted search, citation export, and document download for authorized '
  name: DTIC Discover
  slug: defense-technical-information-center-discover
- description: Authenticated portal for DoD researchers and registered users to access DTIC research and engineering resources, planning documents, and program information.
  name: DTIC Research and Engineering (R&E) Gateway
  slug: defense-technical-information-center-re-gateway
- description: Collaboration platform for DoD scientists, engineers, and program managers operated by DTIC for sharing knowledge, communities of practice, and project information.
  name: DoDTechSpace
  slug: defense-technical-information-center-dodtechspace
- description: Online portal that publishes records released under the Freedom of Information Act. Records are browsable and downloadable but there is no documented API.
  name: DTIC FOIA Reading Room
  slug: defense-technical-information-center-foia
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-technical-information-center-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dod-dtic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defense-technical-information-center
- group: company
  title: ''
  type: Website
  url: https://www.dtic.mil
- group: docs
  title: ''
  type: Documentation
  url: https://www.dtic.mil/about-dtic
- group: company
  title: ''
  type: News
  url: https://www.dtic.mil/dtic-digest
- group: operate
  title: ''
  type: ContactUs
  url: https://www.dtic.mil/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dtic.mil/website-policies
- group: other
  title: ''
  type: FOIA
  url: https://www.dtic.mil/foia
created: '2024-12-25'
description: The Defense Technical Information Center (DTIC) is the U.S. Department of Defense field activity that acquires, manages, and disseminates scientific and technical information from DoD-funded research, development, test, and evaluation. DTIC operates a public Research and Engineering (R&E) Gateway, the Discover service for searching technical reports, the DoDTechSpace and Minsky natural-language platforms for defense researchers, and Dimensions for collaborative discovery. Most DTIC services require authentication tied to DoD or registered-user roles. DTIC does not publicly publish a developer API, though tools such as Dimensions and Minsky offer programmatic capabilities to authorized users.
finops:
- name: Defense Technical Information Center Finops
  service_category: API
  slug: defense-technical-information-center-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-technical-information-center.png
layout: provider
modified: '2026-04-28'
name: Defense Technical Information Center
nav: Providers
network: true
overview: 'Defense Technical Information Center publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Defense, Department of Defense, DTIC, Federal-Government, and Knowledge-Management.


  Defense Technical Information Center''s developer surface includes documentation, product news, and 7 more developer resources.'
plans:
- name: Defense Technical Information Center Plans Pricing
  plan_count: 3
  slug: defense-technical-information-center-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Defense Technical Information Center Rate Limits
  slug: defense-technical-information-center-rate-limits
score:
  band: emerging
  composite: 12.0
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 14.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Defense Technical Information Center Domain Security
  slug: defense-technical-information-center-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: defense-technical-information-center
tags:
- Defense
- Department of Defense
- DTIC
- Federal-Government
- Knowledge-Management
- Library
- Research
- Scientific and Technical Information
website: https://www.dtic.mil
---
