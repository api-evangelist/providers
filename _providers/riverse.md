---
access_model:
  confidence: medium
  label: Customer-only
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://docs.rainbowstandard.io/other/terms-and-contracts/rainbow-standard-and-registry-fees
  - https://rainbowstandard.io/get-started
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
    consent_identity: true
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
  score: 4.7
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riverse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rainbowstandard.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rainbowstandard.io/
- group: start
  title: ''
  type: Registry
  url: https://registry.rainbowstandard.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://rainbowstandard.io/get-started
- group: operate
  title: ''
  type: Support
  url: https://rainbowstandard.io/general-inquiries
- group: company
  title: ''
  type: Blog
  url: https://rainbowstandard.io/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.rainbowstandard.io/other/terms-and-contracts/rainbow-standard-and-registry-fees
- group: commercial
  title: ''
  type: Plans
  url: plans/riverse-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.rainbowstandard.io/other/terms-and-contracts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.rainbowstandard.io/other/terms-and-contracts/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/riverse-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: https://docs.rainbowstandard.io/robots.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/riverse-vocabulary.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/riverse-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.rainbowstandard.io/rainbow-standard-documents/rainbow-standard-rules/version-history
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/riverse-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.rainbowstandard.io/rainbow-standard-documents/procedures-manual/standard-and-methodologies
- group: design
  title: ''
  type: Conformance
  url: conformance/riverse-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.rainbowstandard.io/other/governance-and-integrity
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/riverse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.rainbowstandard.io/rainbow-standard-documents/procedures-manual/registry-requirements
- group: auth
  title: ''
  type: TrustCenter
  url: security/riverse-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.rainbowstandard.io/other/administrative-oversight
coverage:
  checked: '2026-08-17'
  detail: Rainbow's own published fee schedule confirms an API exists — "Rainbow does not charge additional costs for retirement, transfers or API connections" — but the connection is only available to Arc/Registry account holders and not one of the 163 public documentation pages describes an endpoint, base URL, auth model or spec.
  evidence:
  - status: 200
    url: https://docs.rainbowstandard.io/other/terms-and-contracts/rainbow-standard-and-registry-fees.md
  - status: 200
    url: https://docs.rainbowstandard.io/llms.txt
  - status: 404
    url: https://arc.rainbowstandard.io/api/openapi.json
  - status: 404
    url: https://registry.rainbowstandard.io/openapi.json
  - status: 0
    url: https://api.rainbowstandard.io/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'Rainbow — formerly Riverse, whose riverse.io domain now 301s to rainbowstandard.io — is a carbon crediting programme and registry that certifies and issues Rainbow Carbon Credits (RCCs) from engineered carbon removal and greenhouse-gas reduction projects across biochar, BiCRS/BioCCS, enhanced rock weathering, ex-situ mineralization, biogas from anaerobic digestion, biobased construction materials, battery second life and electronics refurbishment. The programme is ICVCM Core-Carbon-Principles approved, ICROA endorsed, approved as a Frontier credit issuer, and runs EU CRCF-compliant plus CORSIA and Paris Agreement Article 6 crediting tracks. It operates two platforms: Arc (arc.rainbowstandard.io), the project-developer certification and MRV platform launched October 2025, and the public Rainbow Registry (registry.rainbowstandard.io) where every project, credit block, serial number and retirement is published. Its public surface is a 163-page GitBook documentation hub of standard
  rules, procedures, methodologies, fees and governance policies, served with a real llms.txt and a Content-Signal AI-usage declaration. No OpenAPI, AsyncAPI, GraphQL SDL, SDK, MCP server or A2A agent card is served on any Rainbow host; the only public acknowledgement that an API exists at all is a single line in the published fee schedule confirming that API connections carry no additional cost.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/riverse.png
layout: provider
modified: '2026-08-17'
name: Rainbow
nav: Providers
network: true
overview: 'Rainbow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Carbon Credits, Carbon Removal, Carbon Markets, and Sustainability.


  Rainbow''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, changelog, and 18 more developer resources.'
plans:
- name: Riverse Plans Pricing
  plan_count: 4
  slug: riverse-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Riverse Rate Limits
  slug: riverse-rate-limits
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.3
    catalog_earned_first_party: 12.0
    catalog_gap: 74.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 22.0
    operational_transparency: 34.2
  previous_composite: 34.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/riverse/refs/heads/main/screenshots/riverse-2026-09-02T153933.png
security:
- kind: domain-security
  name: Riverse Domain Security
  slug: riverse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Riverse Vulnerability Disclosure
  slug: riverse-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Riverse Trust Center
  slug: riverse-trust-center
  summary_line: note, programme, information_security
slug: riverse
tags:
- Company
- Carbon Credits
- Carbon Removal
- Carbon Markets
- Sustainability
- Climate
- Registry
- Certification
- MRV
- Verification
- Biochar
website: https://rainbowstandard.io/
---
