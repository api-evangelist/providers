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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 471
  human_in_the_loop: 9
  name: Cesnet Agentic Access
  operation_count: 989
  slug: cesnet-agentic-access
  summary_line: 989 operations · 471 acting · 9 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: AttributesManager RPC API in Perun
  name: CESNET Attributes Manager API
  slug: cesnet-attributesmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: AuditMessage RPC API in Perun
  name: CESNET Audit Messages Manager API
  slug: cesnet-auditmessagesmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: Endpoints for obtaining and managing API tokens.
  name: CESNET Authorization API
  slug: cesnet-authorization-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: AuthzResolver RPC API in Perun
  name: CESNET Authz Resolver API
  slug: cesnet-authzresolver-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: CabinetManager RPC API in Perun
  name: CESNET Cabinet Manager API
  slug: cesnet-cabinetmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: Choices for rule actions and communities.
  name: CESNET Choices API
  slug: cesnet-choices-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: ConfigManager RPC API in Perun
  name: CESNET Config Manager API
  slug: cesnet-configmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: ConsentsManager RPC API in Perun
  name: CESNET Consents Manager API
  slug: cesnet-consentsmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: DatabaseManager RPC API in Perun
  name: CESNET Database Manager API
  slug: cesnet-databasemanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: ExtSourcesManager RPC API in Perun
  name: CESNET Ext Sources Manager API
  slug: cesnet-extsourcesmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: FacilitiesManager RPC API in Perun
  name: CESNET Facilities Manager API
  slug: cesnet-facilitiesmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: GroupsManager RPC API in Perun
  name: CESNET Groups Manager API
  slug: cesnet-groupsmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: IntegrationManager RPC API in Perun
  name: CESNET Integration Manager API
  slug: cesnet-integrationmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: InvitationsManager RPC API in Perun
  name: CESNET Invitations Manager API
  slug: cesnet-invitationsmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: MembersManager RPC API in Perun
  name: CESNET Members Manager API
  slug: cesnet-membersmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: NotificationManager RPC API in Perun
  name: CESNET Notification Manager API
  slug: cesnet-notificationmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: OwnersManager RPC API in Perun
  name: CESNET Owners Manager API
  slug: cesnet-ownersmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: RegistrarManager RPC API in Perun
  name: CESNET Registrar Manager API
  slug: cesnet-registrarmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: ResourcesManager RPC API in Perun
  name: CESNET Resources Manager API
  slug: cesnet-resourcesmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: RTMessagesManager RPC API in Perun
  name: CESNET RT Messages Manager API
  slug: cesnet-rtmessagesmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: Endpoints for managing IPv4, IPv6, and RTBH rules.
  name: CESNET Rules API
  slug: cesnet-rules-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: Searcher RPC API in Perun
  name: CESNET Searcher API
  slug: cesnet-searcher-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: ServicesManager RPC API in Perun
  name: CESNET Services Manager API
  slug: cesnet-servicesmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: TasksManager RPC API in Perun
  name: CESNET Tasks Manager API
  slug: cesnet-tasksmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: UsersManager RPC API in Perun
  name: CESNET Users Manager API
  slug: cesnet-usersmanager-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: various utilities
  name: CESNET Utils API
  slug: cesnet-utils-api
- baseURL: https://api-dev.perun-aai.org/ba/rpc
  baseurl_source: declared
  description: VosManager RPC API in Perun
  name: CESNET Vos Manager API
  slug: cesnet-vosmanager-api
artifact_total: 42
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/well-known/cesnet-csirt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cesnet-csirt-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/agentic-access/cesnet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cesnet-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/rules/cesnet-rules.yml
  title: ''
  type: Spectral
  url: rules/cesnet-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/rules/cesnet-perun-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/cesnet-perun-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/json-ld/cesnet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cesnet-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/vocabulary/cesnet-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cesnet-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/data-model/cesnet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cesnet-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/cli/cesnet-cli.yml
  title: ''
  type: CLI
  url: cli/cesnet-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/changelog/cesnet-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cesnet-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/conventions/cesnet-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cesnet-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://csirt.cesnet.cz/en/vulnerability_report
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/lifecycle/cesnet-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cesnet-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/lifecycle/cesnet-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cesnet-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/errors/cesnet-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/cesnet-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/errors/cesnet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cesnet-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/conformance/cesnet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cesnet-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/overlays/cesnet-exafs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cesnet-exafs-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/well-known/cesnet-vidcon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cesnet-vidcon-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/well-known/cesnet-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cesnet-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/well-known/cesnet-perun-aai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cesnet-perun-aai-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/well-known/cesnet-du-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cesnet-du-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/well-known/cesnet-api-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cesnet-api-dev-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/well-known/cesnet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cesnet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/hosts/cesnet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cesnet-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/packages/cesnet-packages.yml
  title: ''
  type: SDKs
  url: packages/cesnet-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/packages/cesnet-packages.yml
  title: ''
  type: Packages
  url: packages/cesnet-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.du.cesnet.cz/en/docs/object-storage-rbd/rbd-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.du.cesnet.cz/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/authentication/cesnet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cesnet-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/security/cesnet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cesnet-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/security/cesnet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cesnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cesnet.cz/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cesnet.cz/en/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cesnet.cz/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cesnet.cz/en/gdpr
- group: operate
  title: ''
  type: Support
  url: https://www.cesnet.cz/en/contacts
- group: start
  title: ''
  type: Login
  url: https://muj.cesnet.cz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CESNET
- group: company
  title: ''
  type: LinkedIn
  url: https://cz.linkedin.com/company/cesnet-z.s.p.o
- group: other
  title: ''
  type: X
  url: https://twitter.com/CESNET_cz
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCtnBLNeqJ6wlRK0Dtq5Ch5A
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/CESNET/perun/blob/fde3db50b38f793c941b3cb1fc99ec1b24b8bd88/ruleset-vacuum.yaml
created: '2026-10-09'
description: 'CESNET (CESNET, z.s.p.o., an association of legal entities) is the Czech national research and education network operator, an association of top Czech universities and the Czech Academy of Sciences. It runs the high-performance CESNET3 academic backbone and delivers ICT services to its members: networking, MetaCentrum computing, data storage (FileSender, ownCloud), identity federation and eduroam, multimedia/videoconferencing, and security services, and is part of the e-INFRA CZ research infrastructure. It publishes open-source projects, including the Perun identity and access management system, on GitHub.'
image: https://avatars.githubusercontent.com/u/1116469?v=4
json_schemas:
- name: ApplicationFormItem
  property_count: 17
  slug: cesnet-application-form-item
- name: Application
  property_count: 18
  slug: cesnet-application
- name: ApplicationsPageQuery
  property_count: 13
  slug: cesnet-applications-page-query
- name: PerunNotifTemplate
  property_count: 11
  slug: cesnet-perun-notif-template
- name: Publication
  property_count: 14
  slug: cesnet-publication
- name: RegistrarApplicationInput
  property_count: 4
  slug: cesnet-registrar-application-input
jsonld:
- class_count: 120
  name: Cesnet Context
  property_count: 245
  slug: cesnet-context
layout: provider
modified: '2026-10-09'
name: CESNET
nav: Providers
network: true
overview: 'CESNET publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attributes Manager API, Audit Messages Manager API, Authorization API, and 24 more. Tagged areas include Company, Research and Education Network, Academic Networks, Czech Republic, and High Performance Computing.


  The CESNET catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CESNET''s developer surface includes CLI, changelog, getting-started guide, documentation, authentication, support, YouTube channel, and 36 more developer resources.'
plans:
- name: Cesnet Plans Pricing
  plan_count: 0
  slug: cesnet-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Cesnet Rate Limits
  slug: cesnet-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  - vacuum:owasp
  name: CESNET — perun rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: cesnet-perun-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: CESNET API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 3
  slug: cesnet-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 56.2
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 39.5
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/cesnet/refs/heads/main/screenshots/cesnet-2026-10-11T102831.png
security:
- kind: authentication
  name: Cesnet Authentication
  slug: cesnet-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Cesnet Domain Security
  slug: cesnet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cesnet Vulnerability Disclosure
  slug: cesnet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cesnet
tags:
- Company
- Research and Education Network
- Academic Networks
- Czech Republic
- High Performance Computing
- Data Storage
- Identity Federation
- Cybersecurity
website: https://www.cesnet.cz/
---
