---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 130
  human_in_the_loop: 7
  name: Fastly Agentic Access
  operation_count: 256
  slug: fastly-agentic-access
  summary_line: 256 operations · 130 acting · 7 human-in-the-loop
api_count: 80
apis:
- description: Operations for managing ACL containers within a service version.
  name: Fastly ACL API
  slug: fastly-acl-api
- description: Operations for managing individual entries within an ACL, including IP addresses and CIDR ranges. Entries are versionless and take effect immediately.
  name: Fastly ACL Entry API
  slug: fastly-acl-entry-api
- description: The Alerts API from Fastly — 3 operation(s) for alerts.
  name: Fastly Alerts API
  slug: fastly-alerts-api
- description: Operations for enabling and managing the API Discovery product that identifies API endpoints in service traffic.
  name: Fastly API Discovery API
  slug: fastly-api-discovery-api
- description: Operations for managing automation tokens used by non-human clients such as CI/CD pipelines and build systems.
  name: Fastly Automation Tokens API
  slug: fastly-automation-tokens-api
- description: Operations for managing backends (origin servers) that a Fastly service routes requests to.
  name: Fastly Backend API
  slug: fastly-backend-api
- description: Operations for enabling and managing the Bot Management product on Fastly services.
  name: Fastly Bot Management API
  slug: fastly-bot-management-api
- description: The Buckets API from Fastly — 2 operation(s) for buckets.
  name: Fastly Buckets API
  slug: fastly-buckets-api
- description: Operations for managing cache settings that control cache lifetimes and behavior at the edge.
  name: Fastly Cache Settings API
  slug: fastly-cache-settings-api
- description: The Chat Completions API from Fastly — 2 operation(s) for chat completions.
  name: Fastly Chat Completions API
  slug: fastly-chat-completions-api
- description: Operations for managing conditions that control when configuration objects are applied during request processing.
  name: Fastly Condition API
  slug: fastly-condition-api
- description: Operations for managing config stores that provide low-latency read access to configuration data from Compute services.
  name: Fastly Config Store API
  slug: fastly-config-store-api
- description: The Content Status API from Fastly — 1 operation(s) for content status.
  name: Fastly Content Status API
  slug: fastly-content-status-api
- description: The Custom Dashboards API from Fastly — 2 operation(s) for custom dashboards.
  name: Fastly Custom Dashboards API
  slug: fastly-custom-dashboards-api
- description: Operations for uploading and managing full custom VCL files.
  name: Fastly Custom VCL API
  slug: fastly-custom-vcl-api
- description: Operations for retrieving and updating customer account information.
  name: Fastly Customer API
  slug: fastly-customer-api
- description: Operations for enabling, configuring, and managing DDoS Protection on Fastly services.
  name: Fastly DDoS Protection API
  slug: fastly-ddos-protection-api
- description: Operations for managing dictionary containers within a service version.
  name: Fastly Dictionary API
  slug: fastly-dictionary-api
- description: Operations for retrieving metadata about a dictionary.
  name: Fastly Dictionary Info API
  slug: fastly-dictionary-info-api
- description: Operations for managing individual key-value pairs within a dictionary. Items are versionless and take effect within approximately 30 seconds.
  name: Fastly Dictionary Item API
  slug: fastly-dictionary-item-api
- description: The Diff API from Fastly — 1 operation(s) for diff.
  name: Fastly Diff API
  slug: fastly-diff-api
- description: The Directors API from Fastly — 2 operation(s) for directors.
  name: Fastly Directors API
  slug: fastly-directors-api
- description: The Docs API from Fastly — 1 operation(s) for docs.
  name: Fastly Docs API
  slug: fastly-docs-api
- description: Operations for managing domain associations with Fastly service versions, including DNS validation and configuration checks.
  name: Fastly Domain API
  slug: fastly-domain-api
- description: Domain-level analytics endpoints providing per-domain metrics for Fastly services.
  name: Fastly Domain Inspector API
  slug: fastly-domain-inspector-api
- description: The Embeddings API from Fastly — 1 operation(s) for embeddings.
  name: Fastly Embeddings API
  slug: fastly-embeddings-api
- description: The Events API from Fastly — 2 operation(s) for events.
  name: Fastly Events API
  slug: fastly-events-api
- description: Operations for managing header manipulation rules that add, modify, or remove HTTP headers during request and response processing.
  name: Fastly Header API
  slug: fastly-header-api
- description: Historical statistics endpoints providing aggregated analytics data for Fastly services over configurable time ranges.
  name: Fastly Historical Stats API
  slug: fastly-historical-stats-api
- description: Operations for managing identity and access management roles that define sets of permissions for users.
  name: Fastly IAM Roles API
  slug: fastly-iam-roles-api
- description: Operations for managing service groups that organize services for access control purposes.
  name: Fastly IAM Service Groups API
  slug: fastly-iam-service-groups-api
- description: Operations for managing user groups that organize users and assign them roles and service group access.
  name: Fastly IAM User Groups API
  slug: fastly-iam-user-groups-api
- description: Operations for enabling and managing the Image Optimizer product on Fastly services.
  name: Fastly Image Optimizer API
  slug: fastly-image-optimizer-api
- description: The Insights API from Fastly — 1 operation(s) for insights.
  name: Fastly Insights API
  slug: fastly-insights-api
- description: Operations for managing KV stores that provide persistent key-value storage accessible from Compute services.
  name: Fastly KV Store API
  slug: fastly-kv-store-api
- description: Operations for managing individual items within a KV store.
  name: Fastly KV Store Item API
  slug: fastly-kv-store-item-api
- description: The Log Aggregations API from Fastly — 1 operation(s) for log aggregations.
  name: Fastly Log Aggregations API
  slug: fastly-log-aggregations-api
- description: The Log Explorer API from Fastly — 1 operation(s) for log explorer.
  name: Fastly Log Explorer API
  slug: fastly-log-explorer-api
- description: Operations for managing Google BigQuery logging endpoints on Fastly services.
  name: Fastly Logging BigQuery API
  slug: fastly-logging-bigquery-api
- description: Operations for managing Datadog logging endpoints on Fastly services.
  name: Fastly Logging Datadog API
  slug: fastly-logging-datadog-api
- description: Operations for managing HTTPS logging endpoints on Fastly services.
  name: Fastly Logging HTTPS API
  slug: fastly-logging-https-api
- description: Operations for managing Amazon S3 logging endpoints on Fastly services.
  name: Fastly Logging S3 API
  slug: fastly-logging-s3-api
- description: Operations for managing Splunk logging endpoints on Fastly services.
  name: Fastly Logging Splunk API
  slug: fastly-logging-splunk-api
- description: Operations for managing syslog logging endpoints on Fastly services.
  name: Fastly Logging Syslog API
  slug: fastly-logging-syslog-api
- description: The Notification Service API from Fastly — 2 operation(s) for notification service.
  name: Fastly Notification Service API
  slug: fastly-notification-service-api
- description: The Objects API from Fastly — 2 operation(s) for objects.
  name: Fastly Objects API
  slug: fastly-objects-api
- description: Origin-level analytics endpoints providing metrics about requests to origin servers behind Fastly services.
  name: Fastly Origin Inspector API
  slug: fastly-origin-inspector-api
- description: Operations for managing Compute service packages (WebAssembly binaries).
  name: Fastly Package API
  slug: fastly-package-api
- description: The Pages API from Fastly — 2 operation(s) for pages.
  name: Fastly Pages API
  slug: fastly-pages-api
- description: Operations for managing platform TLS bulk certificates where Fastly manages certificate deployment across the edge network.
  name: Fastly Platform TLS API
  slug: fastly-platform-tls-api
- description: The Policies API from Fastly — 3 operation(s) for policies.
  name: Fastly Policies API
  slug: fastly-policies-api
- description: The POPs API from Fastly — 1 operation(s) for pops.
  name: Fastly POPs API
  slug: fastly-pops-api
- description: The Public IP List API from Fastly — 1 operation(s) for public ip list.
  name: Fastly Public IP List API
  slug: fastly-public-ip-list-api
- description: The Publishing API from Fastly — 1 operation(s) for publishing.
  name: Fastly Publishing API
  slug: fastly-publishing-api
- description: Operations for purging cached content from Fastly's edge network, including single URL purges, surrogate key purges, bulk surrogate key purges, and purge-all operations.
  name: Fastly Purging API
  slug: fastly-purging-api
- description: Real-time analytics endpoints providing second-by-second stats for Fastly services, served from rt.fastly.com.
  name: Fastly Real-Time Analytics API
  slug: fastly-real-time-analytics-api
- description: Operations for managing request settings that modify inbound requests at the edge.
  name: Fastly Request Settings API
  slug: fastly-request-settings-api
- description: Operations for managing synthetic response objects that can be served directly from the edge without contacting an origin.
  name: Fastly Response Object API
  slug: fastly-response-object-api
- description: The Rules API from Fastly — 2 operation(s) for rules.
  name: Fastly Rules API
  slug: fastly-rules-api
- description: The Scripts API from Fastly — 2 operation(s) for scripts.
  name: Fastly Scripts API
  slug: fastly-scripts-api
- description: Operations for managing secret stores that provide encrypted storage for credentials and tokens accessible from Compute services.
  name: Fastly Secret Store API
  slug: fastly-secret-store-api
- description: The Security Headers API from Fastly — 2 operation(s) for security headers.
  name: Fastly Security Headers API
  slug: fastly-security-headers-api
- description: The Server Pools API from Fastly — 2 operation(s) for server pools.
  name: Fastly Server Pools API
  slug: fastly-server-pools-api
- description: The Servers API from Fastly — 2 operation(s) for servers.
  name: Fastly Servers API
  slug: fastly-servers-api
- description: The Service API from Fastly — 4 operation(s) for service.
  name: Fastly Service API
  slug: fastly-service-api
- description: Operations for managing versions of a Fastly service. Each change to a service configuration creates a new version that can be activated or deactivated independently.
  name: Fastly Service Version API
  slug: fastly-service-version-api
- description: The Sudo Mode API from Fastly — 1 operation(s) for sudo mode.
  name: Fastly Sudo Mode API
  slug: fastly-sudo-mode-api
- description: The Timeseries API from Fastly — 1 operation(s) for timeseries.
  name: Fastly Timeseries API
  slug: fastly-timeseries-api
- description: Operations for managing TLS activations that enable TLS traffic termination for specific domains using custom certificates.
  name: Fastly TLS Activations API
  slug: fastly-tls-activations-api
- description: Operations for managing custom TLS certificates that are used to terminate TLS traffic for one or more fully qualified domain names.
  name: Fastly TLS Certificates API
  slug: fastly-tls-certificates-api
- description: Operations for managing private keys used to sign TLS certificates.
  name: Fastly TLS Private Keys API
  slug: fastly-tls-private-keys-api
- description: The Traffic Stats API from Fastly — 1 operation(s) for traffic stats.
  name: Fastly Traffic Stats API
  slug: fastly-traffic-stats-api
- description: Operations for managing user accounts including invitations and profiles.
  name: Fastly User API
  slug: fastly-user-api
- description: Operations for managing user API tokens that authenticate requests to the Fastly API on behalf of a specific user.
  name: Fastly User Tokens API
  slug: fastly-user-tokens-api
- description: Operations for managing VCL snippets, which are small pieces of VCL code that can be inserted into specific subroutines.
  name: Fastly VCL Snippet API
  slug: fastly-vcl-snippet-api
- description: Operations for managing which WAF rules are actively enforced on a firewall.
  name: Fastly WAF Active Rules API
  slug: fastly-waf-active-rules-api
- description: Operations for managing WAF exclusions that prevent specific requests from being flagged by the firewall.
  name: Fastly WAF Exclusions API
  slug: fastly-waf-exclusions-api
- description: Operations for managing WAF firewall instances associated with Fastly services.
  name: Fastly WAF Firewalls API
  slug: fastly-waf-firewalls-api
- description: Operations for managing WAF rules that define detection and response behaviors for web attacks.
  name: Fastly WAF Rules API
  slug: fastly-waf-rules-api
- description: The Websites API from Fastly — 2 operation(s) for websites.
  name: Fastly Websites API
  slug: fastly-websites-api
arazzos:
- description: Clone the active version, create a cache settings rule, then activate the new version.
  name: Fastly Add Cache Settings
  slug: fastly-add-cache-settings-workflow
- description: Clone a version, create a condition, attach a cache settings rule to it, then activate.
  name: Fastly Add Condition and Cache Settings
  slug: fastly-add-condition-and-cache-settings-workflow
- description: Clone the active version, add a new domain to the clone, then activate it.
  name: Fastly Add a Domain to a Service
  slug: fastly-add-domain-to-service-workflow
- description: Clone the active version, add a header manipulation rule, then activate the new version.
  name: Fastly Add a Header Rule
  slug: fastly-add-header-rule-workflow
- description: Clone the active version, insert a VCL snippet, then activate the new version.
  name: Fastly Add a VCL Snippet
  slug: fastly-add-vcl-snippet-workflow
- description: Confirm a service exists, then purge up to 256 surrogate keys in one request.
  name: Fastly Bulk Purge Surrogate Keys
  slug: fastly-bulk-purge-surrogate-keys-workflow
- description: Resolve an ACL by name, then create, update, and delete its entries in one batch.
  name: Fastly Bulk Update ACL Entries
  slug: fastly-bulk-update-acl-entries-workflow
- description: Resolve a dictionary by name, then create, update, upsert, and delete items in one batch.
  name: Fastly Bulk Update Dictionary Items
  slug: fastly-bulk-update-dictionary-items-workflow
- description: Clone the current version, change a backend on the clone, then activate the new version.
  name: Fastly Clone, Update Backend, and Activate
  slug: fastly-clone-version-update-backend-activate-workflow
- description: Create an ACL on a version, activate the version, then add an IP entry to the ACL.
  name: Fastly Create ACL and Add Entry
  slug: fastly-create-acl-and-add-entry-workflow
- description: Create a dictionary on a version, activate it, then add a key-value item.
  name: Fastly Create Dictionary and Add Item
  slug: fastly-create-dictionary-and-add-item-workflow
- description: Search a service by name, read its versions, then clone the active one into a draft.
  name: Fastly Find Service and Clone Active Version
  slug: fastly-find-service-and-clone-active-version-workflow
- description: Create a service, add a draft version, attach a backend and a domain, then activate.
  name: Fastly Provision a Service
  slug: fastly-provision-service-workflow
- description: Upload a key, upload a certificate, then activate TLS for a domain with that certificate.
  name: Fastly Provision TLS Activation
  slug: fastly-provision-tls-activation-workflow
- description: Confirm a service exists, then instantly purge all objects tagged with a surrogate key.
  name: Fastly Purge by Surrogate Key
  slug: fastly-purge-by-surrogate-key-workflow
- description: Branch on the requested scope to either purge a single URL or purge all service content.
  name: Fastly Purge URL or Purge All
  slug: fastly-purge-url-or-all-workflow
- description: Clone the active version, upload a main custom VCL file, then activate the new version.
  name: Fastly Upload Custom VCL
  slug: fastly-upload-custom-vcl-workflow
- description: Upload a TLS private key, then upload the matching custom TLS certificate.
  name: Fastly Upload TLS Key and Certificate
  slug: fastly-upload-tls-key-and-certificate-workflow
- description: Read a domain, then check its DNS configuration and branch on the result.
  name: Fastly Verify Domain DNS
  slug: fastly-verify-domain-dns-workflow
artifact_total: 258
asyncapis:
- description: 'AsyncAPI 2.6 description of the asynchronous and streaming surfaces exposed by Fastly across three documented capabilities: 1. Real-Time Analytics (rt.fastly.com) - long-polling stream of one-second a'
  name: Fastly Streaming, Logging, and Event Surfaces
  slug: fastly-streaming-asyncapi
collections:
- collection_type: postman
  name: Fastly Account API
  slug: postman-fastly-account
- collection_type: postman
  name: Fastly Access Control Lists API
  slug: postman-fastly-acls
- collection_type: postman
  name: Fastly AI Accelerator
  slug: postman-fastly-ai-accelerator
- collection_type: postman
  name: Fastly Authentication Tokens API
  slug: postman-fastly-authentication-tokens
- collection_type: postman
  name: Fastly Client-Side Protection API
  slug: postman-fastly-client-side-protection
- collection_type: postman
  name: Fastly Compute API
  slug: postman-fastly-compute
- collection_type: postman
  name: Fastly DDoS Protection Events API
  slug: postman-fastly-ddos-protection
- collection_type: postman
  name: Fastly Edge Dictionaries API
  slug: postman-fastly-dictionaries
- collection_type: postman
  name: Fastly Domain Management API
  slug: postman-fastly-domain-management
- collection_type: postman
  name: Fastly Load Balancing API
  slug: postman-fastly-load-balancing
- collection_type: postman
  name: Fastly Real-Time Logging API
  slug: postman-fastly-logging
- collection_type: postman
  name: Fastly Metrics and Stats API
  slug: postman-fastly-metrics-and-stats
- collection_type: postman
  name: Fastly Object Storage
  slug: postman-fastly-object-storage
- collection_type: postman
  name: Fastly Observability API
  slug: postman-fastly-observability
- collection_type: postman
  name: Fastly Products API
  slug: postman-fastly-products
- collection_type: postman
  name: Fastly Publishing (Fanout) API
  slug: postman-fastly-publishing
- collection_type: postman
  name: Fastly Purging API
  slug: postman-fastly-purging
- collection_type: postman
  name: Fastly Services API
  slug: postman-fastly-services
- collection_type: postman
  name: Fastly TLS API
  slug: postman-fastly-tls
- collection_type: postman
  name: Fastly Utilities API
  slug: postman-fastly-utilities
- collection_type: postman
  name: Fastly VCL Services API
  slug: postman-fastly-vcl-services
- collection_type: postman
  name: Fastly Next-Gen WAF API
  slug: postman-fastly-waf
- collection_type: open
  name: Fastly Account API
  slug: open-fastly-account
- collection_type: open
  name: Fastly Access Control Lists API
  slug: open-fastly-acls
- collection_type: open
  name: Fastly AI Accelerator
  slug: open-fastly-ai-accelerator
- collection_type: open
  name: Fastly Authentication Tokens API
  slug: open-fastly-authentication-tokens
- collection_type: open
  name: Fastly Client-Side Protection API
  slug: open-fastly-client-side-protection
- collection_type: open
  name: Fastly Compute API
  slug: open-fastly-compute
- collection_type: open
  name: Fastly DDoS Protection Events API
  slug: open-fastly-ddos-protection
- collection_type: open
  name: Fastly Edge Dictionaries API
  slug: open-fastly-dictionaries
- collection_type: open
  name: Fastly Domain Management API
  slug: open-fastly-domain-management
- collection_type: open
  name: Fastly Load Balancing API
  slug: open-fastly-load-balancing
- collection_type: open
  name: Fastly Real-Time Logging API
  slug: open-fastly-logging
- collection_type: open
  name: Fastly Metrics and Stats API
  slug: open-fastly-metrics-and-stats
- collection_type: open
  name: Fastly Object Storage
  slug: open-fastly-object-storage
- collection_type: open
  name: Fastly Observability API
  slug: open-fastly-observability
- collection_type: open
  name: Fastly Products API
  slug: open-fastly-products
- collection_type: open
  name: Fastly Publishing (Fanout) API
  slug: open-fastly-publishing
- collection_type: open
  name: Fastly Purging API
  slug: open-fastly-purging
- collection_type: open
  name: Fastly Services API
  slug: open-fastly-services
- collection_type: open
  name: Fastly TLS API
  slug: open-fastly-tls
- collection_type: open
  name: Fastly Utilities API
  slug: open-fastly-utilities
- collection_type: open
  name: Fastly VCL Services API
  slug: open-fastly-vcl-services
- collection_type: open
  name: Fastly Next-Gen WAF API
  slug: open-fastly-waf
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fastly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fastly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fastly-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fastly/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-add-cache-settings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-add-condition-and-cache-settings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-add-domain-to-service-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-add-header-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-add-vcl-snippet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-bulk-purge-surrogate-keys-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-bulk-update-acl-entries-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-bulk-update-dictionary-items-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-clone-version-update-backend-activate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-create-acl-and-add-entry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-create-dictionary-and-add-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-find-service-and-clone-active-version-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-provision-service-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-provision-tls-activation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-purge-by-surrogate-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-purge-url-or-all-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-upload-custom-vcl-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-upload-tls-key-and-certificate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fastly-verify-domain-dns-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.fastly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fastly.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://www.fastly.com/documentation/reference/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fastly.com/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fastly.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.fastly.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.fastlystatus.com/
- group: operate
  title: ''
  type: Support
  url: https://support.fastly.com/
- group: start
  title: ''
  type: Login
  url: https://manage.fastly.com/account/company
- group: start
  title: ''
  type: Signup
  url: https://www.fastly.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fastly.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fastly.com/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fastly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fastly
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/fastly
- group: build
  title: ''
  type: CLI
  url: https://github.com/fastly/cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/fastly-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/fastly-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/fastly-rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/fastly-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/fastly-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/fastly-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/fastly-perl
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/go-fastly
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/compute-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/js-compute-runtime
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fastly/compute-sdk-python
- group: build
  title: ''
  type: Tools
  url: https://github.com/fastly/terraform-provider-fastly
- group: build
  title: ''
  type: Tools
  url: https://github.com/fastly/Viceroy
- group: build
  title: ''
  type: Tools
  url: https://github.com/fastly/mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/fastly/fastly-agent-toolkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/fastly/fastly-exporter
- group: build
  title: ''
  type: Tools
  url: https://github.com/fastly/vscode-fastly-vcl
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fastly-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fastly-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fastly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fastly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fastly-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-service-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-backend-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-acl-entry-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-dictionary-item-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-tls-certificate-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-ai-accelerator-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-object-storage-object-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fastly-ddos-event-schema.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/fastly-rules.yml
- group: build
  title: ''
  type: Examples
  url: examples/fastly-ai-accelerator-chat-completion-example.json
- group: build
  title: ''
  type: Examples
  url: examples/fastly-object-storage-put-object-example.json
- group: build
  title: ''
  type: Examples
  url: examples/fastly-ddos-protection-list-events-example.json
- group: build
  title: ''
  type: Examples
  url: examples/fastly-observability-alert-definition-example.json
created: '2025-03-01'
description: Fastly is an edge cloud platform that helps customers create great digital experiences quickly, securely, and reliably by processing, serving, and securing their applications closer to their users. The platform spans CDN, Edge Compute (WebAssembly), Object Storage, AI Accelerator (semantic caching for LLMs), AI Bot Management, Next-Gen WAF (Signal Sciences), DDoS Protection, Image Optimizer, Live & Video Streaming, Fanout real-time messaging, and an MCP Server for AI-driven control.
examples:
- key_count: 2
  name: Fastly Ai Accelerator Chat Completion Example
  slug: fastly-ai-accelerator-chat-completion-example
- key_count: 2
  name: Fastly Ddos Protection List Events Example
  slug: fastly-ddos-protection-list-events-example
- key_count: 2
  name: Fastly Object Storage Put Object Example
  slug: fastly-object-storage-put-object-example
- key_count: 2
  name: Fastly Observability Alert Definition Example
  slug: fastly-observability-alert-definition-example
features:
- CDN free tier: 100 GB bandwidth + 1M requests/month
- 'CDN PAYG: $0.08-$0.28/GB and $0.01 per 10K requests (region-tiered)'
- 'Compute free tier: 10M requests + 100M vCPU ms / month'
- 'Compute PAYG: $0.20-$0.50 per 1M requests, $0.02-$0.05 per 1M vCPU ms'
- 'Object Storage free tier: 5 GB / month, zero egress fees'
- 'Object Storage PAYG: $0.017-$0.02/GB, $0.0025 / 1K Class A ops, $0.0004 / 1K Class B ops'
- 'Image Optimizer free tier: 100,000 requests / month'
- 'Image Optimizer PAYG: $0.50-$0.01 per 10K requests'
- 'AI Accelerator free tier: 20,000 requests / month'
- 'AI Accelerator PAYG: $0.40-$0.28 per 1,000 requests'
- 'Domain Research API free tier: 10,000 requests / month'
- 'Basic Package: $1,500/month (100M requests, 20 TLS domains)'
- 'Starter Package: $6,000/month (500M requests, 40 TLS domains)'
- 'Advantage & Ultimate Packages: Contact sales'
- REST API rate limit 1,000 req/hr per token
- 'Purging rate limit: 100,000 / hour per customer (separate from main quota)'
- VCL (Varnish Configuration Language) for edge logic
- WebAssembly Compute platform (Rust, Go, JavaScript, TypeScript, Python)
- Real-time logging to syslog, S3, GCS, BigQuery, Datadog, Splunk, HTTPS
- Image Optimizer for on-the-fly transformations
- Next-Gen WAF (Signal Sciences) with workspaces, signals, virtual patches
- DDoS Protection with events and rules API
- API Security with auto-discovery catalog
- Client-Side Protection (CSP) against Magecart and formjacking
- AI Accelerator semantic caching for OpenAI and Google Gemini
- AI Bot Management to block AI scrapers
- MCP Server for AI-driven Fastly control
- Fanout real-time messaging (GRIP-compatible)
- Object Storage S3-compatible with 11 9s durability
- TLS 1.3 with custom and platform certificates
- 287 public repos in github.com/fastly
finops:
- name: Fastly Finops
  service_category: Edge Network
  slug: fastly-finops
graphqls:
- description: This conceptual GraphQL schema represents the Fastly edge cloud platform API surface. Fastly does not currently expose a native GraphQL endpoint; this schema is a structured representation of the REST
  name: Fastly GraphQL Schema
  slug: fastly-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fastly.png
json_schemas:
- name: Fastly ACL Entry
  property_count: 9
  slug: fastly-acl-entry
- name: Acl
  property_count: 7
  slug: fastly-acl
- name: AclEntry
  property_count: 9
  slug: fastly-aclentry
- name: Fastly AI Accelerator Chat Completion Request
  property_count: 8
  slug: fastly-ai-accelerator-request
- name: AlertDefinition
  property_count: 9
  slug: fastly-alertdefinition
- name: AutomationToken
  property_count: 11
  slug: fastly-automationtoken
- name: Fastly Backend
  property_count: 17
  slug: fastly-backend
- name: BulkTlsCertificate
  property_count: 3
  slug: fastly-bulktlscertificate
- name: CacheSettings
  property_count: 5
  slug: fastly-cachesettings
- name: ChatCompletionRequest
  property_count: 5
  slug: fastly-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 7
  slug: fastly-chatcompletionresponse
- name: Condition
  property_count: 5
  slug: fastly-condition
- name: ConfigStore
  property_count: 4
  slug: fastly-configstore
- name: CspPolicy
  property_count: 3
  slug: fastly-csppolicy
- name: Customer
  property_count: 10
  slug: fastly-customer
- name: CustomVcl
  property_count: 3
  slug: fastly-customvcl
- name: Fastly DDoS Protection Event
  property_count: 7
  slug: fastly-ddos-event
- name: DdosEvent
  property_count: 6
  slug: fastly-ddosevent
- name: DdosProtectionConfiguration
  property_count: 2
  slug: fastly-ddosprotectionconfiguration
- name: DdosRule
  property_count: 5
  slug: fastly-ddosrule
- name: DdosRuleUpdate
  property_count: 2
  slug: fastly-ddosruleupdate
- name: Fastly Dictionary Item
  property_count: 7
  slug: fastly-dictionary-item
- name: Dictionary
  property_count: 8
  slug: fastly-dictionary
- name: DictionaryItem
  property_count: 7
  slug: fastly-dictionaryitem
- name: Domain
  property_count: 7
  slug: fastly-domain
- name: Header
  property_count: 12
  slug: fastly-header
- name: HistoricalStatsResponse
  property_count: 3
  slug: fastly-historicalstatsresponse
- name: Invitation
  property_count: 3
  slug: fastly-invitation
- name: KvStore
  property_count: 4
  slug: fastly-kvstore
- name: LoggingBigQuery
  property_count: 0
  slug: fastly-loggingbigquery
- name: LoggingCommon
  property_count: 5
  slug: fastly-loggingcommon
- name: LoggingDatadog
  property_count: 0
  slug: fastly-loggingdatadog
- name: LoggingHttps
  property_count: 0
  slug: fastly-logginghttps
- name: LoggingS3
  property_count: 0
  slug: fastly-loggings3
- name: LoggingSplunk
  property_count: 0
  slug: fastly-loggingsplunk
- name: LoggingSyslog
  property_count: 0
  slug: fastly-loggingsyslog
- name: Fastly Object Storage Object
  property_count: 9
  slug: fastly-object-storage-object
- name: Package
  property_count: 4
  slug: fastly-package
- name: ProductStatus
  property_count: 3
  slug: fastly-productstatus
- name: PublishItem
  property_count: 4
  slug: fastly-publishitem
- name: PublishRequest
  property_count: 1
  slug: fastly-publishrequest
- name: PurgeResponse
  property_count: 2
  slug: fastly-purgeresponse
- name: RealtimeMeasurements
  property_count: 14
  slug: fastly-realtimemeasurements
- name: RealtimeRecord
  property_count: 3
  slug: fastly-realtimerecord
- name: RealtimeResponse
  property_count: 3
  slug: fastly-realtimeresponse
- name: RequestSettings
  property_count: 12
  slug: fastly-requestsettings
- name: ResponseObject
  property_count: 7
  slug: fastly-responseobject
- name: Role
  property_count: 7
  slug: fastly-role
- name: Script
  property_count: 5
  slug: fastly-script
- name: SecretStore
  property_count: 3
  slug: fastly-secretstore
- name: Fastly Service
  property_count: 10
  slug: fastly-service
- name: ServiceDetail
  property_count: 0
  slug: fastly-servicedetail
- name: ServiceGroup
  property_count: 6
  slug: fastly-servicegroup
- name: ServiceVersion
  property_count: 11
  slug: fastly-serviceversion
- name: Snippet
  property_count: 5
  slug: fastly-snippet
- name: Fastly TLS Certificate
  property_count: 4
  slug: fastly-tls-certificate
- name: TlsActivation
  property_count: 4
  slug: fastly-tlsactivation
- name: TlsCertificate
  property_count: 3
  slug: fastly-tlscertificate
- name: TlsPrivateKey
  property_count: 3
  slug: fastly-tlsprivatekey
- name: Token
  property_count: 11
  slug: fastly-token
- name: User
  property_count: 13
  slug: fastly-user
- name: UserGroup
  property_count: 8
  slug: fastly-usergroup
- name: WafActiveRule
  property_count: 3
  slug: fastly-wafactiverule
- name: WafExclusion
  property_count: 3
  slug: fastly-wafexclusion
- name: WafFirewall
  property_count: 3
  slug: fastly-waffirewall
- name: WafRule
  property_count: 3
  slug: fastly-wafrule
json_structures:
- name: Fastly Structure
  property_count: 0
  slug: fastly-structure
jsonld:
- class_count: 0
  name: Fastly Context
  property_count: 23
  slug: fastly-context
layout: provider
modified: '2026-05-30'
name: Fastly
nav: Providers
network: true
overview: 'Fastly publishes 80 APIs on the [APIs.io](https://apis.io/) network, including ACL API, ACL Entry API, Alerts API, and 77 more. Tagged areas include CDN, Edge Cloud, Edge Compute, WebAssembly, and Security.


  The Fastly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Fastly''s developer surface includes authentication, API reference, documentation, pricing, engineering blog, support, signup flow, and 68 more developer resources.'
plans:
- name: Fastly Plans Pricing
  plan_count: 12
  slug: fastly-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 13
  name: Fastly Rate Limits
  slug: fastly-rate-limits
rules:
- name: Fastly API Rules
  rule_count: 8
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 8
  slug: fastly-asyncapi-spectral-rules
- name: Fastly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fastly-jsonschema-spectral-rules
- name: Fastly API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 2
  slug: fastly-rules
score:
  band: strong
  composite: 65.3
  delta: -8.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 80.0
    developer_ergonomics: 67.4
    discoverability: 68.5
    governance: 62.5
    operational_transparency: 28.9
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 81
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/fastly/refs/heads/main/screenshots/fastly-2026-06-20T181052.png
security:
- kind: authentication
  name: Fastly Authentication
  slug: fastly-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Fastly Domain Security
  slug: fastly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fastly Trust Center
  slug: fastly-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: fastly
tags:
- CDN
- Edge Cloud
- Edge Compute
- WebAssembly
- Security
- AI
- Observability
- AsyncAPI
- Streaming
- Webhooks
- Logging
website: https://www.fastly.com/
---
