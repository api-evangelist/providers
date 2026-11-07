---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Authorities API from Democracy Works — 3 operation(s) for authorities.
  name: Democracy Works Authorities API
  slug: democracy-works-authorities-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Elections API from Democracy Works — 1 operation(s) for elections.
  name: Democracy Works Elections API
  slug: democracy-works-elections-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Exports API from Democracy Works — 1 operation(s) for exports.
  name: Democracy Works Exports API
  slug: democracy-works-exports-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Ballot Measures API from Democracy Works — 1 operation retrieving a single ballot measure by id, with its ballot question, summary, yes/no framing, topics, status and endorsement counts. Sourced f
  name: Democracy Works Ballot Measures API
  slug: democracy-works-ballot-measures-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Candidates API from Democracy Works — 1 operation retrieving a single candidate by id, with party affiliation, incumbency, write-in status, running mate, ranked-choice round and Ballotpedia link.
  name: Democracy Works Candidates API
  slug: democracy-works-candidates-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Contests API from Democracy Works — 1 operation retrieving a single contest by id, with its candidate list, seats up for election, ranked-choice rules, partisan-primary rules and cancellation stat
  name: Democracy Works Contests API
  slug: democracy-works-contests-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: 'The Endorsements API from Democracy Works — 2 operations: one endorsement by id, and endorsements in bulk for a candidate id or a ballot-measure id. Every endorsement carries the endorsing organizatio'
  name: Democracy Works Endorsements API
  slug: democracy-works-endorsements-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Voting Locations API from Democracy Works — 1 operation returning polling places, early-voting sites and ballot drop boxes for a street address, with hours, open/close dates, coordinates, source a
  name: Democracy Works Voting Locations API
  slug: democracy-works-voting-locations-api
- baseURL: https://api.democracy.works/v2
  baseurl_source: declared
  description: The Election Authorities API from Democracy Works — 2 operation(s) for election authorities.
  name: Democracy Works Election Authorities API
  slug: democracy-works-election-authorities-api
artifact_total: 27
collections:
- collection_type: open
  name: Democracy Works Authorities API
  slug: open-democracy-works-authorities-api
- collection_type: open
  name: Democracy Works Elections API
  slug: open-democracy-works-elections-api
- collection_type: open
  name: Democracy Works Exports API
  slug: open-democracy-works-exports-api
common:
- group: other
  href: https://artifacts.apis.io/democracy-works/capabilities/democracy-works-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/democracy-works-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/democracy-works/finops/democracy-works-finops.yml
  title: ''
  type: FinOps
  url: finops/democracy-works-finops.yml
- group: other
  href: https://artifacts.apis.io/democracy-works/overlays/democracy-works-elections-v1-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/democracy-works-elections-v1-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/democracy-works/authentication/democracy-works-authentication.yml
  title: ''
  type: Authentication
  url: authentication/democracy-works-authentication.yml
- group: auth
  href: https://artifacts.apis.io/democracy-works/security/democracy-works-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/democracy-works-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/democracyworks
- group: company
  title: ''
  type: Website
  url: https://www.democracy.works
- group: start
  title: ''
  type: Portal
  url: https://data.democracy.works
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/democracyworks
- group: other
  title: ''
  type: MailingList
  url: https://groups.google.com/a/democracy.works/g/democracy-works-data
- group: operate
  title: ''
  type: Contact
  url: mailto:partnerships@democracy.works
- group: design
  href: https://artifacts.apis.io/democracy-works/json-ld/democracy-works-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/democracy-works-context.jsonld
- group: design
  href: https://artifacts.apis.io/democracy-works/vocabulary/democracy-works-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/democracy-works-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.democracy.works/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.democracy.works/api/v2
- group: docs
  title: ''
  type: Documentation
  url: https://developers.democracy.works/api/v2
- group: docs
  title: ''
  type: APIReference
  url: https://developers.democracy.works/api/v2
- group: operate
  title: ''
  type: StatusPage
  url: https://status.democracy.works
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.democracy.works/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.democracy.works/contact
- group: agent
  href: https://artifacts.apis.io/democracy-works/llms/democracy-works-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/democracy-works-llms.txt
- group: design
  href: https://artifacts.apis.io/democracy-works/conventions/democracy-works-conventions.yml
  title: ''
  type: Conventions
  url: conventions/democracy-works-conventions.yml
- group: design
  href: https://artifacts.apis.io/democracy-works/errors/democracy-works-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/democracy-works-problem-types.yml
- group: design
  href: https://artifacts.apis.io/democracy-works/lifecycle/democracy-works-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/democracy-works-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/democracy-works/changelog/democracy-works-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/democracy-works-changelog.yml
- group: design
  href: https://artifacts.apis.io/democracy-works/data-model/democracy-works-data-model.yml
  title: ''
  type: DataModel
  url: data-model/democracy-works-data-model.yml
- group: design
  href: https://artifacts.apis.io/democracy-works/conformance/democracy-works-conformance.yml
  title: ''
  type: Conformance
  url: conformance/democracy-works-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/democracy-works/plans/democracy-works-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/democracy-works-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/democracy-works/rate-limits/democracy-works-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/democracy-works-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/democracy-works/sandbox/democracy-works-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/democracy-works-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/democracy-works/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/democracy-works/mcp/democracy-works-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/democracy-works-mcp.yml
created: '2024-03-30'
description: Democracy Works is a nonpartisan 501(c)(3) civic technology nonprofit, founded in 2010, that provides Americans with the guidance they need to vote in every election. Its Elections API delivers comprehensive federal, state, county and municipal election data — dates, deadlines, registration and voting methods, contests, candidates, ballot measures, endorsements and polling locations — keyed to Open Civic Data IDs and used by search, social and AI platforms including TikTok, Meta, Perplexity and Anthropic. It also runs TurboVote and co-runs the Voting Information Project with 40+ states.
finops:
- has_sources: true
  method: derived
  name: Democracy Works Finops
  primary_unit: ''
  service_category: ''
  slug: democracy-works-finops
  template: true
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/democracy-works-elections-api-democracy-works-election-data.png
json_schemas:
- name: Authority
  property_count: 6
  slug: democracy-works-authority
- name: Election
  property_count: 8
  slug: democracy-works-election
jsonld:
- class_count: 2
  name: Democracy Works Context
  property_count: 8
  slug: democracy-works-context
layout: provider
modified: '2026-09-07'
name: Democracy Works
nav: Providers
network: true
overview: 'Democracy Works publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorities API, Elections API, Exports API, and 6 more. Tagged areas include Civic Tech, Elections, Government, Non-Profit, and Voter Information.


  The Democracy Works catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Democracy Works'' developer surface includes authentication, developer portal, engineering blog, documentation, API reference, support, changelog, and 25 more developer resources.'
plans:
- name: Democracy Works Plans Pricing
  plan_count: 0
  slug: democracy-works-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Democracy Works Rate Limits
  slug: democracy-works-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Democracy Works — elections api rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: democracy-works-elections-api-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Democracy Works — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: democracy-works-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 45.5
    contract_quality: 61.8
    developer_ergonomics: 55.4
    discoverability: 78.6
    operational_transparency: 26.3
  previous_composite: 46.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/democracy-works/democracy-works-2026-06-20T175910.png
security:
- kind: authentication
  name: Democracy Works Authentication
  slug: democracy-works-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Democracy Works Domain Security
  slug: democracy-works-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: democracy-works-explain-state-voting-rules
  slug: democracy-works-explain-state-voting-rules
- name: democracy-works-explore-the-ballot
  slug: democracy-works-explore-the-ballot
- name: democracy-works-find-upcoming-elections
  slug: democracy-works-find-upcoming-elections
- name: democracy-works-find-where-to-vote
  slug: democracy-works-find-where-to-vote
- name: democracy-works-pull-bulk-exports
  slug: democracy-works-pull-bulk-exports
slug: democracy-works
tags:
- Civic Tech
- Elections
- Government
- Non-Profit
- Voter Information
- Voting
website: https://www.democracy.works
---
