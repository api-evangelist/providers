---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''http://apptimize.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.airship.com/?utm_source=apptimize — a different registrable domain (apptimize.com -> airship.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.apptimize.com
  baseurl_source: declared
  description: Track user events used as experiment and feature-flag goals.
  name: Apptimize Events API
  slug: apptimize-events-api
- baseURL: https://api.apptimize.com
  baseurl_source: declared
  description: Retrieve variant assignments and experiment data for a user.
  name: Apptimize Experiments API
  slug: apptimize-experiments-api
artifact_total: 9
collections:
- collection_type: open
  name: Apptimize REST Events API
  slug: open-apptimize-events-api
- collection_type: open
  name: Apptimize REST Events Experiments API
  slug: open-apptimize-experiments-api
common:
- group: other
  href: https://artifacts.apis.io/apptimize/capabilities/apptimize-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/apptimize-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/airship/
- group: other
  href: https://artifacts.apis.io/apptimize/overlays/apptimize-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apptimize-rest-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://apptimize.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apptimize.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://apptimize.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://apptimize.com/docs/apis/rest-api.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@apptimize.com
- group: build
  href: https://artifacts.apis.io/apptimize/packages/apptimize-packages.yml
  title: ''
  type: Packages
  url: packages/apptimize-packages.yml
- group: build
  href: https://artifacts.apis.io/apptimize/packages/apptimize-packages.yml
  title: ''
  type: SDKs
  url: packages/apptimize-packages.yml
- group: auth
  href: https://artifacts.apis.io/apptimize/authentication/apptimize-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apptimize-authentication.yml
- group: design
  href: https://artifacts.apis.io/apptimize/conventions/apptimize-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apptimize-conventions.yml
- group: design
  href: https://artifacts.apis.io/apptimize/errors/apptimize-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apptimize-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apptimize/lifecycle/apptimize-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apptimize-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/apptimize/mcp/apptimize-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apptimize-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apptimize/llms/apptimize-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apptimize-llms.txt
- group: design
  href: https://artifacts.apis.io/apptimize/conformance/apptimize-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apptimize-conformance.yml
- group: design
  href: https://artifacts.apis.io/apptimize/data-model/apptimize-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apptimize-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apptimize/security/apptimize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apptimize-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/apptimize/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Apptimize is a mobile-first A/B testing, multivariate testing, and feature management platform for optimizing user experiences across iOS, Android, web, and server-side channels. Product teams use Apptimize to run experiments, ship feature flags with controlled rollouts, deliver instant updates without app-store releases, and set dynamic variables that can be changed on the fly. Apptimize ships client and server SDKs for iOS/tvOS/watchOS, Android, Web, React Native, Python, Flutter, and Roku, plus a REST API for retrieving variant assignments and tracking events from any device or backend. Apptimize was acquired by Airship in 2019; its developer documentation and SDKs remain published at apptimize.com/docs, and the marketing site now redirects to airship.com.
image: https://apptimize.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Apptimize
nav: Providers
network: true
overview: 'Apptimize publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Events API and Experiments API. Tagged areas include Company, A/B Testing, Feature Flags, Feature Management, and Experimentation.


  The Apptimize catalog on APIs.io includes 1 Spectral governance ruleset.


  Apptimize''s developer surface includes documentation, API reference, support, authentication, and 16 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Apptimize API Rules
  rule_count: 68
  severity_counts:
    error: 66
    hint: 0
    info: 1
    warn: 1
  slug: apptimize-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 52.3
    developer_ergonomics: 51.8
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 32.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apptimize/apptimize-2026-07-25T200851.png
security:
- kind: authentication
  name: Apptimize Authentication
  slug: apptimize-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apptimize Domain Security
  slug: apptimize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Resolve Apptimize experiments for a user
  slug: apptimize-resolve-experiments
- name: Track an Apptimize event for a user
  slug: apptimize-track-event
slug: apptimize
tags:
- Company
- A/B Testing
- Feature Flags
- Feature Management
- Experimentation
- Mobile
- SDK
- Optimization
website: http://apptimize.com
---
