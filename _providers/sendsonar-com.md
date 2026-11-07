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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Sendsonar Com Agentic Access
  operation_count: 27
  slug: sendsonar-com-agentic-access
  summary_line: 27 operations · 19 acting
api_count: 1
apis:
- description: API for Sonar SMS platform, enabling sending messages, managing customers and teams.
  name: Sonar API
  slug: sonar-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Accounts API from Sonar — 1 operation(s) for accounts.
  name: Sonar Accounts API
  slug: sendsonar-com-accounts-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Campaigns API from Sonar — 2 operation(s) for campaigns.
  name: Sonar Campaigns API
  slug: sendsonar-com-campaigns-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Conversations API from Sonar — 1 operation(s) for conversations.
  name: Sonar Conversations API
  slug: sendsonar-com-conversations-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Customers API from Sonar — 7 operation(s) for customers.
  name: Sonar Customers API
  slug: sendsonar-com-customers-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Events API from Sonar — 1 operation(s) for events.
  name: Sonar Events API
  slug: sendsonar-com-events-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Messages API from Sonar — 3 operation(s) for messages.
  name: Sonar Messages API
  slug: sendsonar-com-messages-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Phone Numbers API from Sonar — 1 operation(s) for phone numbers.
  name: Sonar Phone Numbers API
  slug: sendsonar-com-phone-numbers-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Roles API from Sonar — 1 operation(s) for roles.
  name: Sonar Roles API
  slug: sendsonar-com-roles-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Users API from Sonar — 2 operation(s) for users.
  name: Sonar Users API
  slug: sendsonar-com-users-api
- baseURL: https://www.sendsonar.com/api
  baseurl_source: declared
  description: The Webhooks API from Sonar — 2 operation(s) for webhooks.
  name: Sonar Webhooks API
  slug: sendsonar-com-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Sendsonar Com Webhooks
  slug: sendsonar-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/sendsonar-com/vocabulary/sendsonar-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sendsonar-com-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/sendsonar-com/well-known/sendsonar-com-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sendsonar-com-status-security.txt
- group: agent
  href: https://artifacts.apis.io/sendsonar-com/agentic-access/sendsonar-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sendsonar-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sendsonar-com/rules/sendsonar-com-rules.yml
  title: ''
  type: Spectral
  url: rules/sendsonar-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/sendsonar-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sendsonar-com/asyncapi/sendsonar-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sendsonar-com-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/sendsonar-com/changelog/sendsonar-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sendsonar-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/sendsonar-com/errors/sendsonar-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sendsonar-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sendsonar-com/conformance/sendsonar-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sendsonar-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sendsonar-com/llms/sendsonar-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sendsonar-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/sendsonar-com/well-known/sendsonar-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sendsonar-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/sendsonar-com/hosts/sendsonar-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendsonar-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/sendsonar-com/vendors/sendsonar-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sendsonar-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/sendsonar-com/packages/sendsonar-com-packages.yml
  title: ''
  type: SDKs
  url: packages/sendsonar-com-packages.yml
- group: build
  href: https://artifacts.apis.io/sendsonar-com/packages/sendsonar-com-packages.yml
  title: ''
  type: Packages
  url: packages/sendsonar-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendsonar.com/terms-of-use.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendsonar.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendsonar.com/privacy-policy.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sendsonar.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sendsonar.com/docs/okta-sso-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendsonar
- group: auth
  href: https://artifacts.apis.io/sendsonar-com/authentication/sendsonar-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sendsonar-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sendsonar-com/security/sendsonar-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendsonar-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendsonar.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sendsonar.com
- group: company
  title: ''
  type: Blog
  url: https://blog.sendsonar.com
- group: start
  title: ''
  type: SignUp
  url: https://sendsonar.com/request_demo.html
- group: start
  title: ''
  type: Login
  url: https://dashboard.sendsonar.com
created: '2026-10-25'
description: Sonar provides a Business SMS and Text Messaging platform enabling sales teams to reach customers on their preferred channels, personalize relationships at scale, and close more deals. The customizable solution offers features like Salesforce integration, compliance tools, automation, analytics, and mass texting, supporting industries from automotive to financial services.
image: https://sendsonar.com/images/sonar-logo-og.png
layout: provider
modified: '2026-10-25'
name: Sonar
nav: Providers
network: true
overview: 'Sonar publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Campaigns API, Conversations API, and 8 more. Tagged areas include Company, SMS, Messaging, Sales, and Automation.


  The Sonar catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sonar''s developer surface includes changelog, API reference, getting-started guide, authentication, documentation, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Sonar API Rules
  rule_count: 46
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 7
  slug: sendsonar-com-rules
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 58.5
    developer_ergonomics: 36.3
    discoverability: 64.3
    operational_transparency: 44.7
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/sendsonar-com/sendsonar-com-2026-11-03T143030.png
security:
- kind: authentication
  name: Sendsonar Com Authentication
  slug: sendsonar-com-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sendsonar Com Domain Security
  slug: sendsonar-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: sendsonar-com-add-update-customer-send-campaign
  slug: sendsonar-com-add-update-customer-send-campaign
slug: sendsonar-com
tags:
- Company
- SMS
- Messaging
- Sales
- Automation
website: https://sendsonar.com
---
