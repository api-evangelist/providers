---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-12'
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
- baseURL: https://api.democracy.works
  baseurl_source: declared
  description: The first generation of the Democracy Works Elections API — 3 operations for upcoming elections and state election authorities. Still served at the unversioned base path and still documented (it is wh
  name: Democracy Works Elections API v1 (legacy)
  slug: democracy-works-elections-v1-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: auth
  title: ''
  type: Authentication
  url: authentication/democracy-works-authentication.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/democracy-works-context.jsonld
- group: design
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
  title: ''
  type: LLMsTxt
  url: llms/democracy-works-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/democracy-works-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/democracy-works-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/democracy-works-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/democracy-works-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/democracy-works-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/democracy-works-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/democracy-works-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/democracy-works-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/democracy-works-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/democracy-works-mcp.yml
created: '2024-03-30'
description: Democracy Works is a nonpartisan 501(c)(3) civic technology nonprofit, founded in 2010, that provides Americans with the guidance they need to vote in every election. Its Elections API delivers comprehensive federal, state, county and municipal election data — dates, deadlines, registration and voting methods, contests, candidates, ballot measures, endorsements and polling locations — keyed to Open Civic Data IDs and used by search, social and AI platforms including TikTok, Meta, Perplexity and Anthropic. It also runs TurboVote and co-runs the Voting Information Project with 40+ states.
finops:
- name: Democracy Works Finops
  service_category: API
  slug: democracy-works-finops
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
overview: 'Democracy Works publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authorities API, Elections API, Exports API, and 6 more. Tagged areas include Civic Tech, Elections, Government, Non-Profit, and Voter Information.


  The Democracy Works catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Democracy Works'' developer surface includes authentication, developer portal, engineering blog, documentation, API reference, support, changelog, and 22 more developer resources.'
plans:
- name: Democracy Works Plans Pricing
  plan_count: 0
  slug: democracy-works-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Democracy Works Rate Limits
  slug: democracy-works-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Democracy Works API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: democracy-works-elections-api-rules
- effective_rule_count: 5
  extends: []
  name: Democracy Works API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: democracy-works-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 81.0
    catalog_earned_first_party: 0.0
    catalog_gap: 34.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 87.9
    contract_quality: 68.4
    developer_ergonomics: 55.4
    discoverability: 81.5
    operational_transparency: 26.3
  previous_composite: 56.6
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
    score: 38.9
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/democracy-works/refs/heads/main/screenshots/democracy-works-2026-06-20T175910.png
security:
- kind: authentication
  name: Democracy Works Authentication
  slug: democracy-works-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Democracy Works Domain Security
  slug: democracy-works-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
