---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Production API host operated by 4G Clinical on AWS API Gateway at api.4gclinical.com. Anonymous requests to every probed path return HTTP 403 ForbiddenException, so no route, contract or discovery doc
  name: 4G Clinical API
  slug: 4g-clinical-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.4gclinical.com/
- group: company
  title: ''
  type: Blog
  url: https://www.4gclinical.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.4gclinical.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4GClinical
- group: start
  title: ''
  type: Login
  url: https://portal.4gclinical.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.4gclinical.com/legal
- group: auth
  title: ''
  type: Compliance
  url: https://www.4gclinical.com/trust-center
- group: auth
  title: ''
  type: Security
  url: https://www.4gclinical.com/vulnerability-disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: security/4gclinical-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/4gclinical-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4gclinical-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/4gclinical-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/4gclinical-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/4gclinical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4gclinical-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/4gclinical-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4gclinical-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 4G Clinical runs a live production API host at api.4gclinical.com (AWS API Gateway) that answers HTTP 403 ForbiddenException to every anonymous path including /openapi.json and /.well-known/*, and its 360-URL sitemap contains no developer portal, API reference or machine-readable contract — the 4G DataHub and Enterprise Prancer Integrations surfaces are described only in marketing prose and scoped inside a sponsor engagement.
  evidence:
  - status: 403
    url: https://api.4gclinical.com/openapi.json
  - status: 403
    url: https://api.4gclinical.com/.well-known/oauth-protected-resource
  - status: 200
    url: https://www.4gclinical.com/clinical-data-integrations-reporting
  - status: 404
    url: https://www.4gclinical.com/pricing
  reason: customer-only-docs
  state: gated
created: '2026-09-05'
description: '4G Clinical is a clinical-trial technology company headquartered in Wellesley, Massachusetts, building randomization and trial supply management (RTSM) software for biotech, pharmaceutical and CRO sponsors. Its flagship platform, Prancer RTSM, uses natural language processing to read a written RTSM specification and generate a deployable randomization and supply system, and is sold alongside Prancer Lite for early-phase studies, the Prancer RTSM Inventory Platform for investigator-sponsored trials, 4C Supply for clinical supply forecasting and scenario planning, and 4G DataHub for portfolio-level study data delivery. The company operates a production API host at api.4gclinical.com and markets API-enabled data access, Enterprise Prancer Integrations and EDC/CTMS/depot connectivity, but publishes no public developer portal, API reference or machine-readable contract: integration scope is settled inside a sponsor engagement rather than on the public web.'
image: https://www.4gclinical.com/hubfs/4G-Clinical-logo-black.svg
layout: provider
modified: '2026-09-05'
name: 4G Clinical
nav: Providers
network: true
overview: '4G Clinical publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical Trials, Life Sciences, Randomization, Trial Supply Management, and RTSM.


  4G Clinical''s developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: 4Gclinical Plans Pricing
  plan_count: 0
  slug: 4gclinical-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: 4Gclinical Rate Limits
  slug: 4gclinical-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 13.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4Gclinical Domain Security
  slug: 4gclinical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 4Gclinical Vulnerability Disclosure
  slug: 4gclinical-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: 4Gclinical Trust Center
  slug: 4gclinical-trust-center
  summary_line: SOC 2 Type 2, EU-US Data Privacy Framework (incl. UK Extension and Swiss-US DPF), EcoVadis, United Nations Global Compact
slug: 4gclinical
tags:
- Clinical Trials
- Life Sciences
- Randomization
- Trial Supply Management
- RTSM
- Clinical Supply Chain
- Pharmaceutical
- Healthcare
- Forecasting
- Company
website: https://www.4gclinical.com/
---
