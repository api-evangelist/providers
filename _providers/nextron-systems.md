---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nextron Systems Agentic Access
  operation_count: 7
  slug: nextron-systems-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 2
apis:
- description: The Analysis Cockpit (v4) API; per the manual, "The API documentation has been integrated into the web interface. You can find it in the top right corner's help menu." The reference is served only ins
  name: Analysis Cockpit API
  slug: analysis-cockpit-api
- description: The (Master) Management Center API; per the ASGARD manual it "is documented in the API Documentation section and resembles the API in Management Centers", i.e. inside the appliance web UI, so no publi
  name: ASGARD Management Center API
  slug: asgard-management-center-api
- baseURL: http://localhost:8080/api/v1
  baseurl_source: declared
  description: Endpoints to retrieve information about the running THOR instance
  name: Nextron Systems Info API
  slug: nextron-systems-info-api
- baseURL: http://localhost:8080/api/v1
  baseurl_source: declared
  description: Endpoints to retrieve results of asynchronous scans
  name: Nextron Systems Results API
  slug: nextron-systems-results-api
- baseURL: http://localhost:8080/api/v1
  baseurl_source: declared
  description: Endpoints to scan files with THOR
  name: Nextron Systems Scan API
  slug: nextron-systems-scan-api
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/agentic-access/nextron-systems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nextron-systems-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/rules/nextron-systems-thunderstorm-openapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/nextron-systems-thunderstorm-openapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/rules/nextron-systems-rules.yml
  title: ''
  type: Spectral
  url: rules/nextron-systems-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/json-ld/nextron-systems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nextron-systems-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/vocabulary/nextron-systems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nextron-systems-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/data-model/nextron-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nextron-systems-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/cli/nextron-systems-cli.yml
  title: ''
  type: CLI
  url: cli/nextron-systems-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/conventions/nextron-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nextron-systems-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/authentication/nextron-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nextron-systems-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/lifecycle/nextron-systems-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/nextron-systems-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/lifecycle/nextron-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nextron-systems-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/errors/nextron-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nextron-systems-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/conformance/nextron-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nextron-systems-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/overlays/nextron-systems-thunderstorm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextron-systems-thunderstorm-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/llms/nextron-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nextron-systems-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/hosts/nextron-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nextron-systems-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/packages/nextron-systems-packages.yml
  title: ''
  type: SDKs
  url: packages/nextron-systems-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/packages/nextron-systems-packages.yml
  title: ''
  type: Packages
  url: packages/nextron-systems-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/security/nextron-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nextron-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nextron-systems.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/NextronSystems/thunderstorm-openapi/blob/10b0ca0f8b85a02facf67ef5f07131e239ba460d/.spectral.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://www.nextron-systems.com/resources/manuals/
- group: company
  title: ''
  type: Blog
  url: https://www.nextron-systems.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nextron-systems.com/get-started/
- group: operate
  title: ''
  type: Support
  url: https://support.nextron-systems.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.nextron-systems.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NextronSystems
- group: start
  title: ''
  type: Login
  url: https://portal.nextron-systems.com/
- group: other
  title: ''
  type: FeatureRequests
  url: https://feature-request.nextron-systems.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.nextron-systems.com/category/press/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextron-systems.com/privacy/
- group: other
  title: ''
  type: Imprint
  url: https://www.nextron-systems.com/imprint/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextron-systems
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nextronsystems
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC9lFYoA9MAFhnAzX-AtXFxw
created: '2026-10-09'
description: Nextron Systems (Nextron Systems GmbH) builds automated forensic analysis and compromise assessment tooling under the tagline "We Detect Hackers". Its products include the THOR scanner, THOR Lite, THOR Cloud, THOR Thunderstorm (a web service that scans uploaded samples, with an OpenAPI description published on GitHub), ASGARD Management Center, Analysis Cockpit and the Aurora agent, used to uncover traces of hacking activity, configuration backdoors and obfuscated malware across diverse systems including legacy and edge devices.
image: https://www.nextron-systems.com/wp-content/uploads/2025/10/social-media-large-image-3.png
json_schemas:
- name: AsyncResult
  property_count: 2
  slug: nextron-systems-async-result
- name: SampleIdObj
  property_count: 1
  slug: nextron-systems-sample-id-obj
- name: ThorReport
  property_count: 0
  slug: nextron-systems-thor-report
- name: ThunderstormInfo
  property_count: 6
  slug: nextron-systems-thunderstorm-info
- name: ThunderstormStatus
  property_count: 4
  slug: nextron-systems-thunderstorm-status
jsonld:
- class_count: 7
  name: Nextron Systems Context
  property_count: 19
  slug: nextron-systems-context
layout: provider
modified: '2026-10-09'
name: Nextron Systems
nav: Providers
network: true
overview: 'Nextron Systems publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Info API, Results API, Scan API, and 2 more. Tagged areas include Company, Cybersecurity, Forensics, Compromise Assessment, and Threat Detection.


  The Nextron Systems catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Nextron Systems'' developer surface includes CLI, authentication, documentation, engineering blog, getting-started guide, support, YouTube channel, and 29 more developer resources.'
plans:
- name: Nextron Systems Plans Pricing
  plan_count: 0
  slug: nextron-systems-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Nextron Systems Rate Limits
  slug: nextron-systems-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Nextron Systems API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: nextron-systems-rules
- authorship: provider
  effective_rule_count: 83
  extends:
  - spectral:oas
  - spectral:asyncapi
  - spectral:arazzo
  - '@ibm-cloud/openapi-ruleset'
  name: Nextron Systems — thunderstorm openapi rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: nextron-systems-thunderstorm-openapi-spectral-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 55.3
    catalog_earned_first_party: 0.0
    catalog_gap: 59.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 23.7
    contract_governance: 14.4
    contract_quality: 51.6
    developer_ergonomics: 56.5
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/nextron-systems/refs/heads/main/screenshots/nextron-systems-2026-10-11T111556.png
security:
- kind: authentication
  name: Nextron Systems Authentication
  slug: nextron-systems-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Nextron Systems Domain Security
  slug: nextron-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nextron-systems
tags:
- Company
- Cybersecurity
- Forensics
- Compromise Assessment
- Threat Detection
- Malware Analysis
- Incident Response
website: https://www.nextron-systems.com/
---
