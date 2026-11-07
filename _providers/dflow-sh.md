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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/dflow-sh/plans/dflow-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dflow-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dflow-sh/rules/dflow-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/dflow-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/dflow-sh/vocabulary/dflow-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dflow-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dflow-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dflow-sh/data-model/dflow-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dflow-sh-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.dflow.sh/
- group: auth
  href: https://artifacts.apis.io/dflow-sh/security/dflow-sh-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dflow-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dflow-sh/authentication/dflow-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dflow-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/dflow-sh/conformance/dflow-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dflow-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dflow-sh/llms/dflow-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dflow-sh-llms.txt
- group: auth
  href: https://artifacts.apis.io/dflow-sh/well-known/dflow-sh-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dflow-sh-security.txt
- group: agent
  href: https://artifacts.apis.io/dflow-sh/well-known/dflow-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dflow-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/dflow-sh/hosts/dflow-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dflow-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/dflow-sh/vendors/dflow-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dflow-sh-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dflow.sh/terms
- group: operate
  title: ''
  type: Roadmap
  url: https://dflow.sh/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dflow.sh/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dflow.sh/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dflow-sh
- group: operate
  title: ''
  type: ChangeLog
  url: https://dflow.sh/changelog
- group: company
  title: ''
  type: Blog
  url: https://dflow.sh/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dflow.sh/
- group: auth
  href: https://artifacts.apis.io/dflow-sh/security/dflow-sh-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dflow-sh-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dflow-sh/security/dflow-sh-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dflow-sh-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dflow-sh/security/dflow-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dflow-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dflow.sh/
coverage:
  checked: '2026-11-05'
  detail: Documentation is provided as HTML pages without any OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://docs.dflow.sh
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: dFlow provides a platform to deploy applications and databases in a unified environment, handling infrastructure management so developers can focus on building products. Their service automates provisioning, scaling, and monitoring across cloud providers, offering a seamless experience for modern cloud-native workloads. With a focus on reliability and developer productivity, dFlow aims to simplify the complexities of infrastructure while delivering robust performance and security.
image: https://dflow.sh/logo-mark.svg
layout: provider
modified: '2026-11-05'
name: dFlow
nav: Providers
network: true
overview: 'dFlow publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, Infrastructure, Platform, Deployment, and Automation.


  The dFlow catalog on APIs.io includes 1 Spectral governance ruleset.


  dFlow''s developer surface includes authentication, pricing, changelog, engineering blog, documentation, and 21 more developer resources.'
plans:
- name: Dflow Sh Plans Pricing
  plan_count: 10
  slug: dflow-sh-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: dFlow API Rules
  rule_count: 27
  severity_counts:
    error: 19
    hint: 0
    info: 4
    warn: 4
  slug: dflow-sh-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 44.8
    catalog_earned_first_party: 12.0
    catalog_gap: 70.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 25.6
    discoverability: 48.2
    operational_transparency: 36.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dflow Sh Authentication
  slug: dflow-sh-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dflow Sh Domain Security
  slug: dflow-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dflow Sh Vulnerability Disclosure
  slug: dflow-sh-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dflow Sh Trust Center
  slug: dflow-sh-trust-center
  summary_line: SOC 2, GDPR
skill_count: 1
skills:
- name: getting-started
  slug: dflow-sh-getting-started
slug: dflow-sh
tags:
- Cloud
- Infrastructure
- Platform
- Deployment
- Automation
website: https://dflow.sh/
---
