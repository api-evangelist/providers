---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 253
  human_in_the_loop: 11
  name: Hostinger Agentic Access
  operation_count: 423
  slug: hostinger-agentic-access
  summary_line: 423 operations · 253 acting · 11 human-in-the-loop
api_count: 1
apis:
- description: Hostinger provides a RESTful API for managing hosting services, domains, email, and other resources as documented in their API reference.
  name: Hostinger API
  slug: hostinger-api
artifact_total: 70
asyncapis:
- description: ''
  name: Hostinger Webhooks
  slug: hostinger-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/hostinger/agentic-access/hostinger-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hostinger-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hostinger/rules/hostinger-rules.yml
  title: ''
  type: Spectral
  url: rules/hostinger-rules.yml
- group: design
  href: https://artifacts.apis.io/hostinger/json-ld/hostinger-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hostinger-context.jsonld
- group: design
  href: https://artifacts.apis.io/hostinger/vocabulary/hostinger-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hostinger-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hostinger/asyncapi/hostinger-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hostinger-webhooks.yml
- group: design
  href: https://artifacts.apis.io/hostinger/data-model/hostinger-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hostinger-data-model.yml
- group: auth
  href: https://artifacts.apis.io/hostinger/authentication/hostinger-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hostinger-authentication.yml
- group: design
  href: https://artifacts.apis.io/hostinger/errors/hostinger-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hostinger-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hostinger/conformance/hostinger-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hostinger-conformance.yml
- group: other
  href: https://artifacts.apis.io/hostinger/overlays/hostinger-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hostinger-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/hostinger/well-known/hostinger-statuspage-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hostinger-statuspage-security.txt
- group: commercial
  href: https://artifacts.apis.io/hostinger/plans/hostinger-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hostinger-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hostinger/conventions/hostinger-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hostinger-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.hostinger.com/
- group: auth
  title: ''
  type: Security
  url: https://www.hostinger.com/legal/responsible-disclosure-policy
- group: agent
  href: https://artifacts.apis.io/hostinger/llms/hostinger-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hostinger-llms.txt
- group: auth
  href: https://artifacts.apis.io/hostinger/well-known/hostinger-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hostinger-security.txt
- group: agent
  href: https://artifacts.apis.io/hostinger/well-known/hostinger-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hostinger-well-known.yml
- group: other
  href: https://artifacts.apis.io/hostinger/hosts/hostinger-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hostinger-hosts.yml
- group: other
  href: https://artifacts.apis.io/hostinger/vendors/hostinger-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hostinger-vendors.yml
- group: build
  href: https://artifacts.apis.io/hostinger/packages/hostinger-packages.yml
  title: ''
  type: SDKs
  url: packages/hostinger-packages.yml
- group: build
  href: https://artifacts.apis.io/hostinger/packages/hostinger-packages.yml
  title: ''
  type: Packages
  url: packages/hostinger-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.hostinger.com/templates/ai-coding/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hostinger.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.hostinger.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://auth.hostinger.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hostinger
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.hostinger.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hostinger.com/getting-started/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hostinger.com/api-reference/endpoints.md
- group: auth
  href: https://artifacts.apis.io/hostinger/security/hostinger-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hostinger-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hostinger/security/hostinger-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hostinger-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hostinger/security/hostinger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hostinger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hostinger.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hostinger.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hostinger.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.hostinger.com/
- group: company
  title: ''
  type: Blog
  url: https://www.hostinger.com/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.hostinger.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hostinger.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.hostinger.com/contact
coverage:
  checked: '2026-10-27'
  detail: Documentation is available as HTML pages without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specification.
  evidence:
  - status: 200
    url: https://docs.hostinger.com/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Hostinger is a global web hosting provider offering shared hosting, cloud VPS, domain registration, and a suite of developer tools including an API, CLI, SDKs, and AI-driven services. It serves millions of customers worldwide, providing a control panel (hPanel) for managing websites, email, databases, and cloud resources, with 24/7 support and a 30‑day money‑back guarantee.
image: https://www.hostinger.com/og-image.png
json_schemas:
- name: AgencyHosting.V1.Datacenters.DatacenterCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-datacenters-datacenter-collection
- name: AgencyHosting.V1.Domains.ChangeDomainRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-domains-change-domain-request
- name: AgencyHosting.V1.Domains.DomainCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-domains-domain-collection
- name: AgencyHosting.V1.Domains.LinkDomainRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-domains-link-domain-request
- name: AgencyHosting.V1.Files.ImportArchiveRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-files-import-archive-request
- name: AgencyHosting.V1.Files.UploadUrlResource
  property_count: 3
  slug: hostinger-agency-hosting-v1-files-upload-url-resource
- name: AgencyHosting.V1.Orders.DiskUsageMetrics.MetricsResource
  property_count: 2
  slug: hostinger-agency-hosting-v1-orders-disk-usage-metrics-metrics-resource
- name: AgencyHosting.V1.Orders.OrderCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-orders-order-collection
- name: AgencyHosting.V1.Orders.ResourceUsageMetrics.MetricsResource
  property_count: 3
  slug: hostinger-agency-hosting-v1-orders-resource-usage-metrics-metrics-resource
- name: AgencyHosting.V1.Php.ExtensionCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-php-extension-collection
- name: AgencyHosting.V1.Php.OptionCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-php-option-collection
- name: AgencyHosting.V1.Php.UpdateExtensionsRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-php-update-extensions-request
- name: AgencyHosting.V1.Php.UpdateOptionsRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-php-update-options-request
- name: AgencyHosting.V1.Php.UpdateVersionRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-php-update-version-request
- name: AgencyHosting.V1.Php.VersionCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-php-version-collection
- name: AgencyHosting.V1.Setups.CreateSetupRequest
  property_count: 6
  slug: hostinger-agency-hosting-v1-setups-create-setup-request
- name: AgencyHosting.V1.Setups.WebsiteSetupResource
  property_count: 1
  slug: hostinger-agency-hosting-v1-setups-website-setup-resource
- name: AgencyHosting.V1.Setups.WebsiteSetupStatusResource
  property_count: 2
  slug: hostinger-agency-hosting-v1-setups-website-setup-status-resource
- name: AgencyHosting.V1.Ssl.SslStatusResource
  property_count: 3
  slug: hostinger-agency-hosting-v1-ssl-ssl-status-resource
- name: AgencyHosting.V1.Websites.BuildAssetsRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-websites-build-assets-request
- name: AgencyHosting.V1.Websites.CronJobs.CreateCronJobRequest
  property_count: 2
  slug: hostinger-agency-hosting-v1-websites-cron-jobs-create-cron-job-request
- name: AgencyHosting.V1.Websites.CronJobs.CronJobCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-websites-cron-jobs-cron-job-collection
- name: AgencyHosting.V1.Websites.CronJobs.CronJobResource
  property_count: 4
  slug: hostinger-agency-hosting-v1-websites-cron-jobs-cron-job-resource
- name: AgencyHosting.V1.Websites.Databases.CreateDatabaseRequest
  property_count: 3
  slug: hostinger-agency-hosting-v1-websites-databases-create-database-request
- name: AgencyHosting.V1.Websites.Databases.DatabaseCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-websites-databases-database-collection
- name: AgencyHosting.V1.Websites.Databases.DatabaseResource
  property_count: 3
  slug: hostinger-agency-hosting-v1-websites-databases-database-resource
- name: AgencyHosting.V1.Websites.Databases.DatabaseUserResource
  property_count: 3
  slug: hostinger-agency-hosting-v1-websites-databases-database-user-resource
- name: AgencyHosting.V1.Websites.Databases.Users.CreateDatabaseUserRequest
  property_count: 3
  slug: hostinger-agency-hosting-v1-websites-databases-users-create-database-user-request
- name: AgencyHosting.V1.Websites.WebsiteCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-websites-website-collection
- name: AgencyHosting.V1.Websites.WebsiteProcessCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-websites-website-process-collection
- name: AgencyHosting.V1.Websites.WebsiteResource
  property_count: 16
  slug: hostinger-agency-hosting-v1-websites-website-resource
- name: AgencyHosting.V1.WordPress.ChangeVersionRequest
  property_count: 1
  slug: hostinger-agency-hosting-v1-word-press-change-version-request
- name: AgencyHosting.V1.WordPress.SettingsResource
  property_count: 4
  slug: hostinger-agency-hosting-v1-word-press-settings-resource
- name: AgencyHosting.V1.WordPress.VersionCollection
  property_count: 0
  slug: hostinger-agency-hosting-v1-word-press-version-collection
- name: AgentReadiness.V1.Checks.CheckCollection
  property_count: 0
  slug: hostinger-agent-readiness-v1-checks-check-collection
- name: AgentReadiness.V1.Scans.RunScanRequest
  property_count: 1
  slug: hostinger-agent-readiness-v1-scans-run-scan-request
- name: AgentReadiness.V1.Scans.ScanResource
  property_count: 11
  slug: hostinger-agent-readiness-v1-scans-scan-resource
- name: Billing.V1.Catalog.CatalogItemCollection
  property_count: 0
  slug: hostinger-billing-v1-catalog-catalog-item-collection
- name: Billing.V1.Order.OrderResource
  property_count: 9
  slug: hostinger-billing-v1-order-order-resource
- name: Billing.V1.Order.PaymentProcessingResource
  property_count: 4
  slug: hostinger-billing-v1-order-payment-processing-resource
- name: Billing.V1.Order.PurchaseRequest
  property_count: 3
  slug: hostinger-billing-v1-order-purchase-request
- name: Billing.V1.PaymentMethod.PaymentMethodCollection
  property_count: 0
  slug: hostinger-billing-v1-payment-method-payment-method-collection
- name: Billing.V1.Subscription.Renewal.RenewRequest
  property_count: 2
  slug: hostinger-billing-v1-subscription-renewal-renew-request
- name: Billing.V1.Subscription.SubscriptionCollection
  property_count: 0
  slug: hostinger-billing-v1-subscription-subscription-collection
- name: Billing.V1.Subscription.SubscriptionResource
  property_count: 12
  slug: hostinger-billing-v1-subscription-subscription-resource
- name: Common.Schema.PaginationMetaSchema
  property_count: 3
  slug: hostinger-common-schema-pagination-meta-schema
- name: Common.SuccessEmptyResource
  property_count: 1
  slug: hostinger-common-success-empty-resource
- name: DNS.V1.Snapshot.SnapshotCollection
  property_count: 0
  slug: hostinger-dns-v1-snapshot-snapshot-collection
- name: DNS.V1.Snapshot.SnapshotWithContentResource
  property_count: 4
  slug: hostinger-dns-v1-snapshot-snapshot-with-content-resource
- name: DNS.V1.Zone.DestroyRequest
  property_count: 1
  slug: hostinger-dns-v1-zone-destroy-request
- name: DNS.V1.Zone.RecordCollection
  property_count: 0
  slug: hostinger-dns-v1-zone-record-collection
- name: DNS.V1.Zone.ResetRequest
  property_count: 3
  slug: hostinger-dns-v1-zone-reset-request
- name: DNS.V1.Zone.UpdateRequest
  property_count: 2
  slug: hostinger-dns-v1-zone-update-request
- name: DomainAccessVerifier.V2.Verifications.ActiveVerificationsCollection
  property_count: 1
  slug: hostinger-domain-access-verifier-v2-verifications-active-verifications-collection
- name: DomainAccessVerifier.V2.Verifications.ListRequest
  property_count: 1
  slug: hostinger-domain-access-verifier-v2-verifications-list-request
- name: Domains.V1.Availability.AlternativeCollection
  property_count: 0
  slug: hostinger-domains-v1-availability-alternative-collection
- name: Domains.V1.Availability.AlternativesFromDescriptionRequest
  property_count: 2
  slug: hostinger-domains-v1-availability-alternatives-from-description-request
- name: Domains.V1.Availability.AlternativesFromDomainRequest
  property_count: 2
  slug: hostinger-domains-v1-availability-alternatives-from-domain-request
- name: Domains.V1.Availability.AvailabilityCollection
  property_count: 0
  slug: hostinger-domains-v1-availability-availability-collection
- name: Domains.V1.Availability.AvailabilityRequest
  property_count: 3
  slug: hostinger-domains-v1-availability-availability-request
jsonld:
- class_count: 120
  name: Hostinger Context
  property_count: 236
  slug: hostinger-context
layout: provider
modified: '2026-10-26'
name: Hostinger
nav: Providers
network: true
overview: 'Hostinger publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hosting, Cloud, and Domains.


  The Hostinger catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Hostinger''s developer surface includes authentication, sandbox, changelog, getting-started guide, API reference, documentation, engineering blog, and 34 more developer resources.'
plans:
- name: Hostinger Plans Pricing
  plan_count: 3
  slug: hostinger-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Hostinger API Rules
  rule_count: 64
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 9
  slug: hostinger-rules
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 55.8
    catalog_earned_first_party: 12.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 45.2
    discoverability: 56.3
    operational_transparency: 34.2
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 94
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/hostinger/hostinger-2026-11-03T133456.png
security:
- kind: authentication
  name: Hostinger Authentication
  slug: hostinger-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hostinger Domain Security
  slug: hostinger-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hostinger Vulnerability Disclosure
  slug: hostinger-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Hostinger Trust Center
  slug: hostinger-trust-center
  summary_line: ISO 27001, PCI DSS, GDPR
slug: hostinger
tags:
- Company
- Hosting
- Cloud
- Domains
website: https://www.hostinger.com/
---
