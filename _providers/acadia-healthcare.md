---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'An API gateway host operated by Acadia Healthcare, not a published API product. Probed 2026-08-29: api.acadiahealthcare.com resolves by CNAME to w5rrqr.usa-e2.cloudhub.io (MuleSoft CloudHub, US-East-2'
  name: Acadia Healthcare API Gateway
  slug: acadia-healthcare-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.acadiahealthcare.com
- group: company
  title: ''
  type: Blog
  url: https://www.acadiahealthcare.com/about/news-media-events/
- group: operate
  title: ''
  type: Support
  url: https://www.acadiahealthcare.com/about/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acadiahealthcare.com/about/privacy-practices/online-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acadiahealthcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acadia-healthcare
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadia-healthcare-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/acadia-healthcare-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acadia-healthcare-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acadia-healthcare-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Acadia Healthcare is a behavioral-health hospital operator with no software product to publish — the developer host the catalog previously carried, developer.acadiahealthcare.com, is NXDOMAIN, and the MuleSoft CloudHub gateway that is genuinely deployed at api.acadiahealthcare.com answers every anonymous path, including /openapi.json and every /.well-known/ document, with an empty-body HTTP 404.
  evidence:
  - status: 0
    url: https://developer.acadiahealthcare.com/
  - status: 404
    url: https://api.acadiahealthcare.com/openapi.json
  - status: 404
    url: https://api.acadiahealthcare.com/.well-known/agent-card.json
  - status: 404
    url: https://www.acadiahealthcare.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-04-19'
description: 'Acadia Healthcare Company, Inc. (NASDAQ: ACHC) is a Franklin, Tennessee-based Fortune 1000 behavioral healthcare provider operating a national network of acute inpatient psychiatric hospitals, specialty substance use disorder treatment facilities, residential treatment centers, and outpatient comprehensive treatment clinics across the United States. It is a clinical services operator rather than a software company: as of August 2026 it publishes no developer portal, no API reference, and no machine-readable contract of any kind. A MuleSoft CloudHub gateway is deployed at api.acadiahealthcare.com, but every anonymous path on it returns an empty-body HTTP 404, and the developer host previously recorded here (developer.acadiahealthcare.com) does not resolve. Not to be confused with Acadia Pharmaceuticals (NASDAQ: ACAD), an unrelated company.'
finops:
- name: Acadia Healthcare Finops
  service_category: Behavioral Health Services
  slug: acadia-healthcare-finops
image: /assets/icons/acadia-healthcare.png
layout: provider
modified: '2026-08-29'
name: Acadia Healthcare
nav: Providers
network: true
overview: 'Acadia Healthcare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health, Mental Health, Substance Use Treatment, Healthcare Providers, and Hospitals.


  Acadia Healthcare''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Acadia Healthcare Plans Pricing
  plan_count: 0
  slug: acadia-healthcare-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Acadia Healthcare Rate Limits
  slug: acadia-healthcare-rate-limits
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 15.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acadia-healthcare/refs/heads/main/screenshots/acadia-healthcare-2026-08-07T160746.png
security:
- kind: domain-security
  name: Acadia Healthcare Domain Security
  slug: acadia-healthcare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acadia-healthcare
tags:
- Behavioral Health
- Mental Health
- Substance Use Treatment
- Healthcare Providers
- Hospitals
- Fortune 1000
website: https://www.acadiahealthcare.com
---
