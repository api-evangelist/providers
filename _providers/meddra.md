---
access_model:
  confidence: high
  label: Annual subscription - free for regulatory authorities and non-profits, sliding-scale fee for commercial
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 31.8
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meddra Agentic Access
  operation_count: 16
  slug: meddra-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://mapisbx.meddra.org
  baseurl_source: declared
  description: The MedDRA API published by the MSSO — term and SMQ search, term/SMQ detail, hierarchy navigation and analysis, parent/child type lookup, term history, SMQ analysis, data-file download, search export,
  name: MedDRA API
  slug: meddra-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.meddra.org/
- group: start
  title: ''
  type: Portal
  url: https://www.meddra.org/meddra-apis
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.meddra.org/meddra-apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.meddra.org/meddra-apis
- group: docs
  title: ''
  type: APIReference
  url: https://mapisbx.meddra.org/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.meddra.org/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meddra.org/subscription-rates
- group: start
  title: ''
  type: SignUp
  url: https://www.meddra.org/subscription/subscription-form
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meddra-msso
- group: other
  title: ''
  type: X-Downloads
  url: https://www.meddra.org/software-packages
- group: start
  title: ''
  type: Console
  url: https://mapisbx.meddra.org/index.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/authentication/meddra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meddra-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/scopes/meddra-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/meddra-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/well-known/meddra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meddra-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/security/meddra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meddra-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/conventions/meddra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/meddra-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/errors/meddra-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meddra-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/lifecycle/meddra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/meddra-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/changelog/meddra-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/meddra-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/conformance/meddra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meddra-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/conformance/meddra-conformance.yml
  title: ''
  type: Compliance
  url: conformance/meddra-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/sandbox/meddra-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/meddra-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/data-model/meddra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meddra-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/packages/meddra-packages.yml
  title: ''
  type: Packages
  url: packages/meddra-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/llms/meddra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meddra-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/overlays/meddra-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/meddra-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/mcp/meddra-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/meddra-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/agentic-access/meddra-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meddra-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/plans/meddra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meddra-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/rate-limits/meddra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/meddra-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/finops/meddra-finops.yml
  title: ''
  type: FinOps
  url: finops/meddra-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/rules/meddra-jsonschema-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/meddra-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/json-schema/meddra-term-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/json-ld/meddra-context.jsonld
created: '2026-05-03'
description: 'MedDRA (Medical Dictionary for Regulatory Activities) is the clinically validated international medical terminology developed under the auspices of the International Council for Harmonisation (ICH) and used by regulatory authorities and the regulated biopharmaceutical industry for adverse event coding, drug safety reporting and pharmacovigilance. It is maintained by the MedDRA Maintenance and Support Services Organization (MSSO), which publishes a new version twice a year in English and more than a dozen translations. The MSSO operates a REST API programme so subscribers can embed MedDRA term search, hierarchy navigation (SOC, HLGT, HLT, PT, LLT), SMQ analysis, version-impact reporting and subscription validation in their own pharmacovigilance and clinical systems. Two API environments are operated: a GxP-assessed one carrying four APIs for validated systems, and a wider non-GxP environment carrying sixteen. Access requires an MSSO subscription.'
finops:
- name: Meddra Finops
  service_category: API
  slug: meddra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meddra.png
json_schemas:
- name: MedDRA Term
  property_count: 9
  slug: meddra-term
jsonld:
- class_count: 2
  name: Meddra Context
  property_count: 13
  slug: meddra-context
layout: provider
modified: '2026-09-17'
name: Meddra
nav: Providers
network: true
overview: 'Meddra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Terminology, Pharmacovigilance, Drug Safety, Adverse Events, and Regulatory.


  The Meddra catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Meddra''s developer surface includes developer portal, documentation, API reference, support, pricing, signup flow, developer console, and 28 more developer resources.'
plans:
- name: Meddra Plans Pricing
  plan_count: 11
  slug: meddra-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Meddra Rate Limits
  slug: meddra-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Meddra API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: meddra-jsonschema-spectral-rules
scopes:
- name: Meddra Scopes
  scope_count: 3
  slug: meddra-scopes
  summary_line: 3 scopes · implicit
score:
  band: developing
  composite: 51.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 69.3
    catalog_earned_first_party: 12.0
    catalog_gap: 45.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.6
  facets:
    access_clarity: 71.1
    contract_governance: 28.0
    contract_quality: 49.7
    developer_ergonomics: 42.3
    discoverability: 68.5
    operational_transparency: 15.8
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 48.8
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/meddra/refs/heads/main/screenshots/meddra-2026-06-20T185114.png
security:
- kind: authentication
  name: Meddra Authentication
  slug: meddra-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Meddra Domain Security
  slug: meddra-domain-security
  summary_line: TLSv1.3
slug: meddra
tags:
- Medical Terminology
- Pharmacovigilance
- Drug Safety
- Adverse Events
- Regulatory
- Clinical Trials
- Healthcare
- Life Sciences
- Standards
- Ontology
website: https://www.meddra.org/
---
