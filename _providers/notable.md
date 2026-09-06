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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.notablehealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.notablehealth.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/notablehealth
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.notablehealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.notablehealth.com/terms-of-use
- group: auth
  title: ''
  type: TrustCenter
  url: security/notable-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.notablehealth.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.notablehealth.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/notable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notable-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.notablehealth.com/contact
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/notable-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/notable-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/notable-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/notable-lifecycle.yml
coverage:
  checked: '2026-08-15'
  detail: Notable's only developer documentation host, docs.notablehealth.com, 307-redirects every path — including /openapi.json, /docs.json, /llms.txt and /api-reference — to https://app.notablehealth.com/mintlify/sso, which then 302s to the Notable staff application login, so the Mintlify API reference is readable only by authenticated customers.
  evidence:
  - status: 307
    url: https://docs.notablehealth.com/openapi.json
  - status: 302
    url: https://app.notablehealth.com/mintlify/sso?redirect=%2F
  - status: 404
    url: https://api.notablehealth.com/openapi.json
  - status: 200
    url: https://www.notablehealth.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Notable is an intelligent-automation company purpose-built for healthcare, applying AI agents to administrative and operational workflows across patient access, revenue cycle management, care operations, and contact-center automation. Its platform pairs a library of prebuilt AI Agents with Flow Builder, a low-code interface for designing, training, and deploying automations, Sidekick, a human-in-the-loop AI co-pilot for clinically complex work such as prior authorization, and Flow AI, a conversational assistant for workflow builders. Integration runs bi-directionally against Epic, Oracle Health/Cerner, MEDITECH, athenahealth and eClinicalWorks over a mix of FHIR APIs, HL7 interfaces, RPA and third-party APIs. Notable reports deployment at 12,000+ sites of care serving 38M+ patients, with customers including Intermountain Health, MUSC Health, CommonSpirit Health and CityMD, and is backed by ICONIQ Growth, Greylock, F-Prime, Oak HC/FT, Maverick Ventures and 8VC. Notable publishes
  no public API contract; its developer documentation sits behind customer SSO. This profile is enriched from the company's public trust, security, and llms.txt surfaces.
image: https://cdn.prod.website-files.com/628b58b14c93b9187d929a89/67b78b8f557320958bb3f989_notable_logo.svg
layout: provider
modified: '2026-08-15'
name: Notable
nav: Providers
network: true
overview: 'Notable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Application, Healthcare, Artificial Intelligence, and Automation.


  Notable''s developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Notable Plans Pricing
  plan_count: 0
  slug: notable-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Notable Rate Limits
  slug: notable-rate-limits
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 21.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notable/refs/heads/main/screenshots/notable-2026-08-07T185548.png
security:
- kind: domain-security
  name: Notable Domain Security
  slug: notable-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Notable Vulnerability Disclosure
  slug: notable-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Notable Trust Center
  slug: notable-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, PCI DSS, HITRUST
slug: notable
tags:
- Company
- Application
- Healthcare
- Artificial Intelligence
- Automation
- Revenue Cycle
- Patient Access
- Agents
- Prior Authorization
- EHR Integration
- FHIR
- Contact Center
- Care Operations
website: https://www.notablehealth.com/
---
