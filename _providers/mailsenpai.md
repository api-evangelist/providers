---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Mailsenpai Agentic Access
  operation_count: 13
  slug: mailsenpai-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://app.mailsenpai.com/relay/v1
  baseurl_source: declared
  description: The Account API from SMTP Senpai (MailSenpai) — 1 operation(s) for account.
  name: SMTP Senpai (MailSenpai) Account API
  slug: mailsenpai-account-api
- baseURL: https://app.mailsenpai.com/relay/v1
  baseurl_source: declared
  description: The Log API from SMTP Senpai (MailSenpai) — 2 operation(s) for log.
  name: SMTP Senpai (MailSenpai) Log API
  slug: mailsenpai-log-api
- baseURL: https://app.mailsenpai.com/relay/v1
  baseurl_source: declared
  description: The Sending API from SMTP Senpai (MailSenpai) — 1 operation(s) for sending.
  name: SMTP Senpai (MailSenpai) Sending API
  slug: mailsenpai-sending-api
- baseURL: https://app.mailsenpai.com/relay/v1
  baseurl_source: declared
  description: The SMTP Senpai API API from SMTP Senpai (MailSenpai) — 0 operation(s) for smtp senpai api.
  name: SMTP Senpai (MailSenpai) SMTP Senpai API
  slug: mailsenpai-smtp-senpai-api-api
- baseURL: https://app.mailsenpai.com/relay/v1
  baseurl_source: declared
  description: The Suppression API from SMTP Senpai (MailSenpai) — 3 operation(s) for suppression.
  name: SMTP Senpai (MailSenpai) Suppression API
  slug: mailsenpai-suppression-api
- baseURL: https://app.mailsenpai.com/relay/v1
  baseurl_source: declared
  description: The Webhooks API from SMTP Senpai (MailSenpai) — 2 operation(s) for webhooks.
  name: SMTP Senpai (MailSenpai) Webhooks API
  slug: mailsenpai-webhooks-api
- baseURL: https://app.mailsenpai.com/relay/v1
  baseurl_source: declared
  description: The Website forms API from SMTP Senpai (MailSenpai) — 1 operation(s) for website forms.
  name: SMTP Senpai (MailSenpai) Website forms API
  slug: mailsenpai-website-forms-api
artifact_total: 20
asyncapis:
- description: ''
  name: Mailsenpai Webhooks
  slug: mailsenpai-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/agentic-access/mailsenpai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailsenpai-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/plans/mailsenpai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailsenpai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/rules/mailsenpai-rules.yml
  title: ''
  type: Spectral
  url: rules/mailsenpai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/json-ld/mailsenpai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailsenpai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/vocabulary/mailsenpai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailsenpai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/asyncapi/mailsenpai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mailsenpai-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/data-model/mailsenpai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailsenpai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/conventions/mailsenpai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mailsenpai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/conventions/mailsenpai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mailsenpai-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/authentication/mailsenpai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailsenpai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/errors/mailsenpai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mailsenpai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/conformance/mailsenpai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailsenpai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/llms/mailsenpai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailsenpai-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/well-known/mailsenpai-gitlab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mailsenpai-gitlab-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/well-known/mailsenpai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailsenpai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/hosts/mailsenpai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailsenpai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/vendors/mailsenpai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mailsenpai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/packages/mailsenpai-packages.yml
  title: ''
  type: SDKs
  url: packages/mailsenpai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/packages/mailsenpai-packages.yml
  title: ''
  type: Packages
  url: packages/mailsenpai-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.mailsenpai.com/customer/guest/register?lang=en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mailsenpai/refs/heads/main/security/mailsenpai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailsenpai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.mailsenpai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://en.mailsenpai.com/smtp-api/
- group: docs
  title: ''
  type: APIReference
  url: https://en.mailsenpai.com/smtp-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://en.mailsenpai.com/smtp-senpai/
- group: operate
  title: ''
  type: Support
  url: https://en.mailsenpai.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://en.mailsenpai.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://en.mailsenpai.com/plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.mailsenpai.com/tc/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.mailsenpai.com/privacy-policy/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://en.mailsenpai.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: 'MailSenpai is an Italian email service for businesses, operating since 2016 with servers and data hosted in the European Union. It offers two products: an email marketing platform for newsletters and campaigns, and SMTP Senpai, a transactional email relay service with REST API and SMTP access. The service supports Italian and English support, provides DKIM signing, SPF/DKIM/DMARC checks, and detailed sending logs. Plans are tiered with a free trial and pricing in euros, targeting B2B outreach and marketing automation.'
image: https://en.mailsenpai.com/wp-content/uploads/2026/10/mailsenpai-og-en.jpg
json_schemas:
- name: Conteggi
  property_count: 11
  slug: mailsenpai-conteggi
- name: Evento
  property_count: 11
  slug: mailsenpai-evento
- name: InvioMulti
  property_count: 6
  slug: mailsenpai-invio-multi
- name: InvioRichiesta
  property_count: 17
  slug: mailsenpai-invio-richiesta
- name: ModuloCampi
  property_count: 6
  slug: mailsenpai-modulo-campi
- name: Stato
  property_count: 6
  slug: mailsenpai-stato
jsonld:
- class_count: 16
  name: Mailsenpai Context
  property_count: 77
  slug: mailsenpai-context
layout: provider
modified: '2026-10-12'
name: SMTP Senpai (MailSenpai)
nav: Providers
network: true
overview: 'SMTP Senpai (MailSenpai) publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Log API, Sending API, and 4 more. Tagged areas include Email marketing, B2B outreach, SMTP relay, Artificial intelligence, and Newsletter platform.


  The SMTP Senpai (MailSenpai) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  SMTP Senpai (MailSenpai)''s developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
plans:
- name: Mailsenpai Plans Pricing
  plan_count: 4
  slug: mailsenpai-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: SMTP Senpai (MailSenpai) API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: mailsenpai-rules
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 70.0
    developer_ergonomics: 56.5
    discoverability: 73.2
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Mailsenpai Authentication
  slug: mailsenpai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mailsenpai Domain Security
  slug: mailsenpai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mailsenpai
tags:
- Email marketing
- B2B outreach
- SMTP relay
- Artificial intelligence
- Newsletter platform
website: https://en.mailsenpai.com/
---
