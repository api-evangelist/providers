---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: https://api.flexera.com
  baseurl_source: declared
  description: The Content API from CloudCheckr — 1 operation(s) for content.
  name: CloudCheckr Content API
  slug: cloudcheckr-content-api
- baseURL: https://api.flexera.com
  baseurl_source: declared
  description: The Iam API from CloudCheckr — 1 operation(s) for iam.
  name: CloudCheckr Iam API
  slug: cloudcheckr-iam-api
- baseURL: https://api.flexera.com
  baseurl_source: declared
  description: The Msp API from CloudCheckr — 1 operation(s) for msp.
  name: CloudCheckr Msp API
  slug: cloudcheckr-msp-api
- baseURL: https://api.flexera.com
  baseurl_source: declared
  description: The Oidc API from CloudCheckr — 1 operation(s) for oidc.
  name: CloudCheckr Oidc API
  slug: cloudcheckr-oidc-api
artifact_total: 11
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/rate-limits/cloudcheckr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudcheckr-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/rules/cloudcheckr-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudcheckr-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/json-ld/cloudcheckr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudcheckr-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/vocabulary/cloudcheckr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudcheckr-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/data-model/cloudcheckr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudcheckr-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/conventions/cloudcheckr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudcheckr-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/authentication/cloudcheckr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudcheckr-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/conformance/cloudcheckr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudcheckr-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/llms/cloudcheckr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudcheckr-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/well-known/cloudcheckr-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloudcheckr-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/well-known/cloudcheckr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudcheckr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/hosts/cloudcheckr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudcheckr-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/vendors/cloudcheckr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudcheckr-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flexera.com/
- group: auth
  title: ''
  type: Security
  url: https://www.flexera.com/products/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flexera.com/legal/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.flexera.com/about-us/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.flexera.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.flexera.com/docs/api/finops-onboarding/v1
- group: docs
  title: ''
  type: Documentation
  url: https://developer.flexera.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudcheckr/refs/heads/main/security/cloudcheckr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudcheckr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flexera.com/products/cloudcheckr
coverage:
  checked: '2026-10-09'
  detail: Developer portal returns HTML shells for OpenAPI endpoints, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://developer.cloudcheckr.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: CloudCheckr provides cloud cost management and optimization solutions for managed service providers and enterprises. It helps organizations identify wasted spend, control AI costs, reduce Kubernetes expenses, and allocate cloud costs across business units. As part of Flexera, CloudCheckr delivers unified visibility, governance, and risk management across multi-cloud environments, enabling FinOps and operational efficiency.
image: https://www.flexera.com/themes/custom/flexera/images/flexera_social.png
json_schemas:
- name: PostContentV2OrgsYourRequest
  property_count: 1
  slug: cloudcheckr-post-content-v2-orgs-your-request
- name: PostOidcTokenResponse
  property_count: 4
  slug: cloudcheckr-post-oidc-token-response
jsonld:
- class_count: 2
  name: Cloudcheckr Context
  property_count: 5
  slug: cloudcheckr-context
layout: provider
modified: '2026-10-09'
name: CloudCheckr
nav: Providers
network: true
overview: 'CloudCheckr is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Content API, Iam API, Msp API, and 1 more. Tagged areas include Company, Cloud Cost Management, FinOps, MSP, and Enterprise.


  The CloudCheckr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CloudCheckr''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Cloudcheckr Rate Limits
  slug: cloudcheckr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: CloudCheckr API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cloudcheckr-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 67.8
    catalog_earned_first_party: 8.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 21.6
    developer_ergonomics: 35.7
    discoverability: 80.4
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cloudcheckr Authentication
  slug: cloudcheckr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cloudcheckr Domain Security
  slug: cloudcheckr-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cloudcheckr
tags:
- Company
- Cloud Cost Management
- FinOps
- MSP
- Enterprise
- Flexera
website: https://www.flexera.com/products/cloudcheckr
---
