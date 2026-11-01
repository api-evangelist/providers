---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Snorkel Flow Python SDK (snorkelflow) drives the platform programmatically, connecting to a customer's Snorkel Flow instance via SnorkelFlowContext and an API key. The snorkelflow.client module wr
  name: Snorkel Flow SDK / Platform
  slug: snorkel-flow-sdk-platform
- description: SDK surface (snorkelflow.studio, snorkelflow.lfs, snorkelflow.operators, snorkelflow.templates) for authoring code-based and template-based labeling functions, transformation and slicing functions, an
  name: Programmatic Labeling
  slug: programmatic-labeling
- description: Platform and SDK capabilities for assessing model performance across data splits, running error and slice analysis, and building expert-curated benchmarks. Largely delivered in-platform and through th
  name: Evaluation
  slug: evaluation
- description: The free, open-source snorkel Python library (Apache-2.0) for programmatically building and managing training data with weak supervision - labeling functions, the LabelModel, transformation functions,
  name: Open-Source Snorkel Library
  slug: open-source-snorkel-library
- baseURL_template: https://{snorkelInstance}
  baseurl_source: spec_template
  description: Each customer's Snorkel instance exposes a REST API (the snorkelai.sdk.client module is documented as "Interfaces to interact with the Snorkel REST API") at its own per-instance URL, authenticated wit
  name: Snorkel Platform REST API
  slug: snorkel-platform-rest-api
artifact_total: 15
collections:
- collection_type: open
  name: Snorkel Flow Platform API
  slug: open-snorkel-ai
common:
- group: design
  href: https://artifacts.apis.io/snorkel-ai/rules/snorkel-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/snorkel-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/snorkel-ai/vocabulary/snorkel-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snorkel-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/snorkel-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/snorkel-ai/conventions/snorkel-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snorkel-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.snorkel.ai/
- group: auth
  href: https://artifacts.apis.io/snorkel-ai/security/snorkel-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/snorkel-ai-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/snorkel-ai/lifecycle/snorkel-ai-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/snorkel-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/snorkel-ai/lifecycle/snorkel-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snorkel-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/snorkel-ai/conformance/snorkel-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snorkel-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/snorkel-ai/overlays/snorkel-ai-openapi-generated-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snorkel-ai-openapi-generated-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/snorkel-ai/llms/snorkel-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snorkel-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/snorkel-ai/well-known/snorkel-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snorkel-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/snorkel-ai/well-known/snorkel-ai-customer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snorkel-ai-customer-security.txt
- group: agent
  href: https://artifacts.apis.io/snorkel-ai/well-known/snorkel-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snorkel-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/snorkel-ai/hosts/snorkel-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snorkel-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/snorkel-ai/integrations/snorkel-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/snorkel-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/snorkel-ai/vendors/snorkel-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/snorkel-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/snorkel-ai/packages/snorkel-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/snorkel-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/snorkel-ai/packages/snorkel-ai-packages.yml
  title: ''
  type: Packages
  url: packages/snorkel-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/snorkel-ai/security/snorkel-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/snorkel-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/snorkel-ai/security/snorkel-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/snorkel-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snorkel-ai/security/snorkel-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snorkel-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/snorkel-ai/authentication/snorkel-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snorkel-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snorkel-team
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snorkel-ai
- group: company
  title: ''
  type: Website
  url: https://snorkel.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snorkel.ai
- group: commercial
  href: https://artifacts.apis.io/snorkel-ai/finops/snorkel-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/snorkel-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://snorkel.ai/blog/
- group: other
  title: ''
  type: RSSFeed
  url: https://snorkel.ai/feed/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.snorkel.ai/docs/26.7/sdk/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snorkel.ai/docs/26.7/user-guide/sdk/quick_start/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.snorkel.ai/release-notes/v261-release-notes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snorkel.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snorkel.ai/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://snorkel.ai/press/
- group: operate
  title: ''
  type: Contact
  url: https://snorkel.ai/contact/
- group: company
  title: ''
  type: Careers
  url: https://snorkel.ai/join-us/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/snorkelai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC6MQ2p8gZFYdTLEV8cysE6Q
coverage:
  checked: '2026-10-27'
  detail: Snorkel says its SDK wraps a per-instance REST API, but it publishes no OpenAPI or other contract and documents only one HTTP endpoint (GET /audit-logs) verbatim, so the only contract is generated from that page.
  evidence:
  - status: 200
    url: https://docs.snorkel.ai/docs/26.7/sdk/autosummary/snorkelai.sdk.client
  - status: 200
    url: https://docs.snorkel.ai/docs/26.7/administration/settings-and-administration/reviewing-audit-logs
  - status: 404
    url: https://docs.snorkel.ai/openapi.json
  - status: 404
    url: https://docs.snorkel.ai/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-06-21'
description: Snorkel AI is a data-development / AI data platform built on the open-source Snorkel weak-supervision library. The enterprise Snorkel Flow platform supports programmatic labeling, data curation, model training, and evaluation, and is driven programmatically through a Python SDK that targets a per-instance REST API rather than a single public hosted endpoint. Snorkel also delivers Expert Data-as-a-Service for frontier-model training and evaluation data.
finops:
- has_sources: true
  method: generated
  name: Snorkel Ai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: snorkel-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snorkel-ai.png
layout: provider
modified: '2026-10-27'
name: Snorkel AI
nav: Providers
network: true
overview: 'Snorkel AI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Snorkel Platform REST API, and 4 more. Tagged areas include Artificial Intelligence, Data Development, Programmatic Labeling, Weak Supervision, and Evaluation.


  The Snorkel AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Snorkel AI''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, release notes, YouTube channel, and 33 more developer resources.'
plans:
- name: Snorkel Ai Plans Pricing
  plan_count: 0
  slug: snorkel-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Snorkel Ai Rate Limits
  slug: snorkel-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Snorkel AI API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: snorkel-ai-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.0
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 11.1
    developer_ergonomics: 51.8
    discoverability: 58.9
    operational_transparency: 39.5
  previous_composite: 28.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/snorkel-ai/snorkel-ai-2026-09-02T160025.png
security:
- kind: authentication
  name: Snorkel Ai Authentication
  slug: snorkel-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Snorkel Ai Domain Security
  slug: snorkel-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snorkel Ai Vulnerability Disclosure
  slug: snorkel-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Snorkel Ai Trust Center
  slug: snorkel-ai-trust-center
  summary_line: SOC 2, HIPAA
skill_count: 1
skills:
- name: snorkel-ai-review-audit-logs
  slug: snorkel-ai-review-audit-logs
slug: snorkel-ai
tags:
- Artificial Intelligence
- Data Development
- Programmatic Labeling
- Weak Supervision
- Evaluation
- SDK
website: https://snorkel.ai
---
