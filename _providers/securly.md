---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Credential-gated MDM API that lets an approved third-party asset or device-management system pull an inventory list of devices (iPads, Macs, Apple TVs) managed in Securly MDM. Access is provisioned pe
  name: Securly MDM Device Inventory API
  slug: securly-mdm-device-inventory-api
- description: Credential-gated MDM API that lets an approved third-party system assign or unassign students to and from devices managed in Securly MDM. Uses the same per-tenant API connection credentials (Client ID
  name: Securly MDM Student Assignment API
  slug: securly-mdm-student-assignment-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/securly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/securly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.securly.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/securly
- group: docs
  title: ''
  type: Documentation
  url: https://docs.securly.com/
- group: operate
  title: ''
  type: Support
  url: https://support.securly.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/securly-plans-pricing.yml
created: '2026-07-04'
description: Securly is a K-12 student safety company whose platform spans web filtering, device management (MDM), classroom management, and student wellness/self-harm and threat monitoring across the web, email, and cloud drives. Securly is deployed by school districts and integrates with the school technology stack - Google Workspace, Microsoft 365/Entra, Apple School Manager, and Student Information Systems via the OneRoster and rostering standards. Securly's public developer surface is limited and access-gated - it primarily CONSUMES rostering and identity APIs from external systems rather than exposing a documented public developer API. The one provider-exposed API is a credential-gated Securly MDM API used by third-party device/asset systems to pull device inventory and assign or unassign students to devices; its endpoints and base URL are provisioned per tenant and are not publicly documented as a reference.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/securly.png
layout: provider
modified: '2026-07-04'
name: Securly
nav: Providers
network: true
overview: 'Securly publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include K-12, Education, EdTech, Student Safety, and Web Filtering.


  Securly''s developer surface includes documentation, support, and 5 more developer resources.'
plans:
- name: Securly Plans Pricing
  plan_count: 0
  slug: securly-plans-pricing
random_paper: 19
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/securly/refs/heads/main/screenshots/securly-2026-09-02T154725.png
security:
- kind: domain-security
  name: Securly Domain Security
  slug: securly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Securly Vulnerability Disclosure
  slug: securly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: securly
tags:
- K-12
- Education
- EdTech
- Student Safety
- Web Filtering
- Device Management
- MDM
- Wellness Monitoring
- Rostering
- OneRoster
- Gated API
website: https://www.securly.com/
---
