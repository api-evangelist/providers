---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 74
  human_in_the_loop: 1
  name: Argorant Com Agentic Access
  operation_count: 142
  slug: argorant-com-agentic-access
  summary_line: 142 operations · 74 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Who the key acts as, the plan, the credit balance, the request limits and the scopes. Free to call.
  name: Argorant Account API
  slug: argorant-com-account-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Email addresses and whole domains your campaigns never contact. A block covers every campaign of the workspace, or only the campaigns you name. Add or remove up to 5,000 at a time, with a dry run that
  name: Argorant Blocklist API
  slug: argorant-com-blocklist-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Email outreach from start to finish. Create a campaign, write the emails, add people, choose the sending mailboxes and launch. Nothing sends until you launch.
  name: Argorant Campaigns API
  slug: argorant-com-campaigns-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Count and preview companies, and see how many people Argorant has at one company. Free.
  name: Argorant Companies API
  slug: argorant-com-companies-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Buy credits from a script or an agent. Get a quote, show it to the person who pays, then buy only after their yes. The saved card is charged within the limits the workspace set, or you get a payment l
  name: Argorant Credits API
  slug: argorant-com-credits-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Find a person's work email from their name and company domain, one at a time or as a list. 1 credit when found, 1 credit for a domain that accepts every address (the email is marked unconfirmed), 0.25
  name: Argorant Email finder API
  slug: argorant-com-email-finder-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: 'Fill in one record you already have: an email, a name at a company, or a company domain.'
  name: Argorant Enrich API
  slug: argorant-com-enrich-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: CSV files of checked contacts. Every email is checked when the file is built and you pay only for the ones that pass.
  name: Argorant Exports API
  slug: argorant-com-exports-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Every reply across your campaigns in one place. Read a conversation, answer in the same thread, forward it, and set a status such as interested or meeting booked, including your own pipeline stages.
  name: Argorant Inbox API
  slug: argorant-com-inbox-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Send people into the sending tool you already use, in your own account there. Connect the tool once in Settings, Connected tools with its API key, then send a campaign's people or an export into one o
  name: Argorant Integrations API
  slug: argorant-com-integrations-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Saved lists of people. A list is a search you keep or the people you picked. Export a list, add it to a campaign, or add more people to it.
  name: Argorant Lists API
  slug: argorant-com-lists-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: 'Free word lists for the search filters: industries, countries, keywords, technologies and job titles, each with how many contacts match.'
  name: Argorant Lookups API
  slug: argorant-com-lookups-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: The mailboxes that send your campaigns. List and change them, connect a whole Google Workspace in one step, connect a mailbox from any other email provider with its server settings, or order new mailb
  name: Argorant Mailboxes API
  slug: argorant-com-mailboxes-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Count and preview the people who fit your filters for free, then reveal their checked work emails and phone numbers. You pay only for contacts whose email passes the check.
  name: Argorant People API
  slug: argorant-com-people-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: Check the emails on your own list before you send. Get a free quote, then start the check. Half a credit per address checked; addresses checked recently are free.
  name: Argorant Verification API
  slug: argorant-com-verification-api
- baseURL: https://app.argorant.com
  baseurl_source: declared
  description: 'Get a signed HTTP call when something happens: a reply, a positive reply, a bounce, an export that is ready. Included from the Pro plan.'
  name: Argorant Webhooks API
  slug: argorant-com-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Argorant Com Webhooks
  slug: argorant-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/argorant-com/agentic-access/argorant-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/argorant-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/argorant-com/rate-limits/argorant-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/argorant-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/argorant-com/plans/argorant-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/argorant-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/rules/argorant-com-rules.yml
  title: ''
  type: Spectral
  url: rules/argorant-com-rules.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/json-ld/argorant-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/argorant-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/argorant-com/vocabulary/argorant-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/argorant-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/argorant-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/asyncapi/argorant-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/argorant-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/data-model/argorant-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/argorant-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/argorant-com/cli/argorant-com-cli.yml
  title: ''
  type: CLI
  url: cli/argorant-com-cli.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/conventions/argorant-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/argorant-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/conventions/argorant-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/argorant-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/argorant-com/authentication/argorant-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/argorant-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/lifecycle/argorant-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/argorant-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/errors/argorant-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/argorant-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/argorant-com/conformance/argorant-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/argorant-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/argorant-com/llms/argorant-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/argorant-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/argorant-com/well-known/argorant-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/argorant-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/argorant-com/hosts/argorant-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/argorant-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/argorant-com/packages/argorant-com-packages.yml
  title: ''
  type: Packages
  url: packages/argorant-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://argorant.com/status
- group: build
  title: ''
  type: SDKs
  url: https://argorant.com/b2b-leads/by-industry/libraries
- group: operate
  title: ''
  type: Roadmap
  url: https://argorant.com/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/argorant
- group: operate
  title: ''
  type: ChangeLog
  url: https://argorant.com/changelog
- group: auth
  href: https://artifacts.apis.io/argorant-com/security/argorant-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/argorant-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://argorant.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.argorant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.argorant.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.argorant.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.argorant.com/docs/guides/your-first-call
- group: operate
  title: ''
  type: Support
  url: https://argorant.com/help
- group: company
  title: ''
  type: Blog
  url: https://argorant.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://argorant.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://argorant.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://argorant.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.argorant.com/signup
created: '2026-11-01'
description: Argorant provides B2B outreach powered by AI, offering verified contact data, email verification, and campaign automation. The platform lets users find the right people, check every email, set up mailboxes, and run campaigns directly from the app or via Claude and ChatGPT. It offers a free trial, flexible pricing plans, and detailed documentation for developers.
image: https://argorant.com/argorant-favicon-padded-white-512.png
json_schemas:
- name: CampaignSummary
  property_count: 19
  slug: argorant-com-campaign-summary
- name: Company
  property_count: 19
  slug: argorant-com-company
- name: CreditPurchase
  property_count: 12
  slug: argorant-com-credit-purchase
- name: Export
  property_count: 25
  slug: argorant-com-export
- name: Mailbox
  property_count: 13
  slug: argorant-com-mailbox
- name: Person
  property_count: 19
  slug: argorant-com-person
jsonld:
- class_count: 33
  name: Argorant Com Context
  property_count: 200
  slug: argorant-com-context
layout: provider
modified: '2026-11-01'
name: Argorant
nav: Providers
network: true
overview: 'Argorant publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Blocklist API, Campaigns API, and 13 more. Tagged areas include B2B, Data, Email Verification, Artificial Intelligence, and Outreach.


  The Argorant catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Argorant''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Argorant Com Plans Pricing
  plan_count: 5
  slug: argorant-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Argorant Com Rate Limits
  slug: argorant-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Argorant API Rules
  rule_count: 71
  severity_counts:
    error: 63
    hint: 0
    info: 1
    warn: 7
  slug: argorant-com-rules
scopes:
- name: Argorant Com Scopes
  scope_count: 0
  slug: argorant-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.3
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 76.0
    developer_ergonomics: 55.2
    discoverability: 66.1
    operational_transparency: 60.5
  previous_composite: 73.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Argorant Com Authentication
  slug: argorant-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Argorant Com Domain Security
  slug: argorant-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: list-people
  slug: argorant-com-list-people
slug: argorant-com
tags:
- B2B
- Data
- Email Verification
- Artificial Intelligence
- Outreach
- Software-as-a-Service
website: https://argorant.com/
---
