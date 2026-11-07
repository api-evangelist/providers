---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Domeneschluse No Agentic Access
  operation_count: 22
  slug: domeneschluse-no-agentic-access
  summary_line: 22 operations · 7 acting
api_count: 1
apis:
- description: The App API from Domeneschluse — 10 operation(s) for app.
  name: Domeneschluse App API
  slug: domeneschluse-no-app-api
- description: The Healthz API from Domeneschluse — 1 operation(s) for healthz.
  name: Domeneschluse Healthz API
  slug: domeneschluse-no-healthz-api
- description: The Historikk API from Domeneschluse — 3 operation(s) for historikk.
  name: Domeneschluse Historikk API
  slug: domeneschluse-no-historikk-api
- description: The Koble Til API from Domeneschluse — 3 operation(s) for koble til.
  name: Domeneschluse Koble Til API
  slug: domeneschluse-no-koble-til-api
- description: The Mcp API from Domeneschluse — 1 operation(s) for mcp.
  name: Domeneschluse MCP API
  slug: domeneschluse-no-mcp-api
- description: The Samtykke API from Domeneschluse — 1 operation(s) for samtykke.
  name: Domeneschluse Samtykke API
  slug: domeneschluse-no-samtykke-api
- description: The .well Known API from Domeneschluse — 1 operation(s) for .well known.
  name: Domeneschluse .well Known API
  slug: domeneschluse-no-well-known-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/domeneschluse-no/agentic-access/domeneschluse-no-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/domeneschluse-no-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/domeneschluse-no/rules/domeneschluse-no-rules.yml
  title: ''
  type: Spectral
  url: rules/domeneschluse-no-rules.yml
- group: design
  href: https://artifacts.apis.io/domeneschluse-no/json-ld/domeneschluse-no-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/domeneschluse-no-context.jsonld
- group: design
  href: https://artifacts.apis.io/domeneschluse-no/vocabulary/domeneschluse-no-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/domeneschluse-no-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/domeneschluse-no/data-model/domeneschluse-no-data-model.yml
  title: ''
  type: DataModel
  url: data-model/domeneschluse-no-data-model.yml
- group: design
  href: https://artifacts.apis.io/domeneschluse-no/errors/domeneschluse-no-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/domeneschluse-no-problem-types.yml
- group: design
  href: https://artifacts.apis.io/domeneschluse-no/conformance/domeneschluse-no-conformance.yml
  title: ''
  type: Conformance
  url: conformance/domeneschluse-no-conformance.yml
- group: agent
  href: https://artifacts.apis.io/domeneschluse-no/llms/domeneschluse-no-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domeneschluse-no-llms.txt
- group: agent
  href: https://artifacts.apis.io/domeneschluse-no/well-known/domeneschluse-no-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domeneschluse-no-well-known.yml
- group: other
  href: https://artifacts.apis.io/domeneschluse-no/hosts/domeneschluse-no-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domeneschluse-no-hosts.yml
- group: other
  href: https://artifacts.apis.io/domeneschluse-no/vendors/domeneschluse-no-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domeneschluse-no-vendors.yml
- group: auth
  href: https://artifacts.apis.io/domeneschluse-no/security/domeneschluse-no-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domeneschluse-no-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domeneschluse.no/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domeneschluse.no/personvern
- group: start
  title: ''
  type: GettingStarted
  url: https://domeneschluse.no/koble-til
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://domeneschluse.no/openapi.json
  - status: null
    url: https://api.domeneschluse.no/openapi.json
  - status: 401
    url: https://domeneschluse.no/mcp
  - status: 401
    url: https://api.domeneschluse.no/mcp
  - status: 200
    url: https://domeneschluse.no/
  reason: partner-login
  state: gated
created: '2026-11-05'
description: Domeneschluse provides a free MCP server that connects your Domeneshop email account to AI assistants like Claude. It offers IMAP/SMTP access, DNS management, and transparent data handling, with OAuth 2.1 authentication and detailed privacy information. The service is hosted in Frankfurt and aims to give users AI‑enhanced email capabilities.
image: https://domeneschluse.no/og.png
json_schemas:
- name: ApiNoekkelId
  property_count: 1
  slug: domeneschluse-no-api-noekkel-id
- name: ApiNoekkel
  property_count: 3
  slug: domeneschluse-no-api-noekkel
- name: SjekkInn
  property_count: 1
  slug: domeneschluse-no-sjekk-inn
- name: VerifiserInn
  property_count: 2
  slug: domeneschluse-no-verifiser-inn
jsonld:
- class_count: 6
  name: Domeneschluse No Context
  property_count: 12
  slug: domeneschluse-no-context
layout: provider
modified: '2026-11-05'
name: Domeneschluse
nav: Providers
network: true
overview: 'Domeneschluse publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including App API, Healthz API, Historikk API, and 4 more. Tagged areas include Company, Email, Artificial Intelligence, MCP, and Open Source.


  The Domeneschluse catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Domeneschluse''s developer surface includes getting-started guide and 14 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Domeneschluse API Rules
  rule_count: 33
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 2
  slug: domeneschluse-no-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.7
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domeneschluse No Domain Security
  slug: domeneschluse-no-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: domeneschluse-no
tags:
- Company
- Email
- Artificial Intelligence
- MCP
- Open Source
- Privacy
website: https://domeneschluse.no/
---
