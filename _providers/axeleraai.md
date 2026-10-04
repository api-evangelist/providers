---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.2
  scored_at: '2026-10-03'
api_count: 2
apis:
- description: SDK for Axelera AI hardware, providing model zoo and inference tools.
  name: Axelera AI SDK
  slug: axelera-ai-sdk
- baseURL: https://software.axelera.ai
  baseurl_source: declared
  description: The Artifactory API from Axeleraai — 5 operation(s) for artifactory.
  name: Axeleraai Artifactory API
  slug: axeleraai-artifactory-api
artifact_total: 7
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/rules/axeleraai-rules.yml
  title: ''
  type: Spectral
  url: rules/axeleraai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/json-ld/axeleraai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/axeleraai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/vocabulary/axeleraai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/axeleraai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/data-model/axeleraai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/axeleraai-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/changelog/axeleraai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/axeleraai-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://axelera.ai/vulnerability-disclosure-policy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/conformance/axeleraai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axeleraai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/llms/axeleraai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axeleraai-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/well-known/axeleraai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axeleraai-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/well-known/axeleraai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axeleraai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/hosts/axeleraai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axeleraai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/vendors/axeleraai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axeleraai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.axelera.ai/site/terms
- group: start
  title: ''
  type: SignUp
  url: https://community.axelera.ai/member/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://axelera.ai/privacy-policy?hsLang=en
- group: company
  title: ''
  type: Newsroom
  url: https://axelera.ai/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axelera-ai-hub
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.axelera.ai/sdk/release-notes
- group: company
  title: ''
  type: Blog
  url: https://axelera.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.axelera.ai/sdk/reference/models/model-zoo
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axelera.ai/sdk/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axelera.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/security/axeleraai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/axeleraai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axeleraai/refs/heads/main/security/axeleraai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axeleraai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axelera.ai
coverage:
  checked: 2026-09-27
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.axelera.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Axeleraai (Axelera AI) develops high‑performance AI accelerators and edge computing solutions, offering hardware such as the Metis and Europa AI processors, a comprehensive SDK (Voyager), model zoo, and enterprise‑grade software. The company focuses on datacenter performance, edge efficiency, and sovereign AI, targeting industries like manufacturing, healthcare, and robotics. Their products span embedded, edge, and server form‑factors, emphasizing low power consumption, high TOPS per watt, and on‑device data privacy.
image: https://axelera.ai/hubfs/Axelera-White-header-logo-right-space-2.svg
json_schemas:
- name: GetArtifactoryAxeleraWinPackages18X18XidResponse
  property_count: 1
  slug: axeleraai-get-artifactory-axelera-win-packages18-x18-xid-response
jsonld:
- class_count: 1
  name: Axeleraai Context
  property_count: 0
  slug: axeleraai-context
layout: provider
modified: '2026-09-27'
name: Axeleraai
nav: Providers
network: true
overview: 'Axeleraai publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Artifactory API, and 1 more. Tagged areas include Company, Artificial Intelligence, Hardware, Edge Computing, and Data Center.


  The Axeleraai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Axeleraai''s developer surface includes changelog, signup flow, engineering blog, API reference, getting-started guide, documentation, and 19 more developer resources.'
random_paper: 16
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Axeleraai API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: axeleraai-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Axeleraai Domain Security
  slug: axeleraai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Axeleraai Vulnerability Disclosure
  slug: axeleraai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: axeleraai
tags:
- Company
- Artificial Intelligence
- Hardware
- Edge Computing
- Data Center
website: https://axelera.ai
---
