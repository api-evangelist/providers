---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Logz.io alerts use a Kibana search query to continuously scan your logs and alert you when a certain set of conditions is met. The simplest alerts can use a simple search query or a particular filter,
  name: Logz.io Alerts API
  slug: logz-io-alerts-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: You can archive logs to an AWS S3 bucket or Azure Blob Storage. Archiving gives you the option to restore logs and query them after they have expired from your time-based account. You can use the foll
  name: Logz.io Archive logs API
  slug: logz-io-archive-logs-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Associated accounts API from Logz.io — 1 operation(s) for associated accounts.
  name: Logz.io Associated accounts API
  slug: logz-io-associated-accounts-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Before you can use Authentication Groups API, Logz.io support will need to enable [SSO](https://docs.logz.io/user-guide/users/single-sign-on/) for your account.
  name: Logz.io Authentication groups API
  slug: logz-io-authentication-groups-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Establish a connection to ship logs to the Logz.io observability platform via an S3 bucket. Supports CloudTrail logs.
  name: Logz.io Connect to CloudTrail API
  slug: logz-io-connect-to-cloudtrail-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Establish a connection for the Logz.io fetcher to fetch logs to the Logz.io observability platform via an S3 bucket. Supports ELB, S3 Access, CloudFront, VPC Flow logs. If you're looking to fetch Clou
  name: Logz.io Connect to S3 Buckets API
  slug: logz-io-connect-to-s3-buckets-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards create new API from Logz.io — 1 operation(s) for dashboards create new.
  name: Logz.io Dashboards create new API
  slug: logz-io-dashboards-create-new-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards create new folder API from Logz.io — 1 operation(s) for dashboards create new folder.
  name: Logz.io Dashboards create new folder API
  slug: logz-io-dashboards-create-new-folder-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards delete API from Logz.io — 1 operation(s) for dashboards delete.
  name: Logz.io Dashboards delete API
  slug: logz-io-dashboards-delete-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards delete folder API from Logz.io — 1 operation(s) for dashboards delete folder.
  name: Logz.io Dashboards delete folder API
  slug: logz-io-dashboards-delete-folder-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards get all API from Logz.io — 1 operation(s) for dashboards get all.
  name: Logz.io Dashboards get all API
  slug: logz-io-dashboards-get-all-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards get all folders API from Logz.io — 1 operation(s) for dashboards get all folders.
  name: Logz.io Dashboards get all folders API
  slug: logz-io-dashboards-get-all-folders-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards get all global data sources API from Logz.io — 1 operation(s) for dashboards get all global data sources.
  name: Logz.io Dashboards get all global data sources API
  slug: logz-io-dashboards-get-all-global-data-sources-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards get by ID API from Logz.io — 1 operation(s) for dashboards get by id.
  name: Logz.io Dashboards get by ID API
  slug: logz-io-dashboards-get-by-id-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards get by user API from Logz.io — 1 operation(s) for dashboards get by user.
  name: Logz.io Dashboards get by user API
  slug: logz-io-dashboards-get-by-user-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards get folder by name API from Logz.io — 1 operation(s) for dashboards get folder by name.
  name: Logz.io Dashboards get folder by name API
  slug: logz-io-dashboards-get-folder-by-name-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards move API from Logz.io — 1 operation(s) for dashboards move.
  name: Logz.io Dashboards move API
  slug: logz-io-dashboards-move-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards rename folder API from Logz.io — 1 operation(s) for dashboards rename folder.
  name: Logz.io Dashboards rename folder API
  slug: logz-io-dashboards-rename-folder-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards search folder API from Logz.io — 1 operation(s) for dashboards search folder.
  name: Logz.io Dashboards search folder API
  slug: logz-io-dashboards-search-folder-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards update API from Logz.io — 1 operation(s) for dashboards update.
  name: Logz.io Dashboards update API
  slug: logz-io-dashboards-update-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Dashboards update folder API from Logz.io — 1 operation(s) for dashboards update folder.
  name: Logz.io Dashboards update folder API
  slug: logz-io-dashboards-update-folder-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Delete object API API from Logz.io — 1 operation(s) for delete object api.
  name: Logz.io Delete object API
  slug: logz-io-delete-object-api-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Send deployment logs by API to automatically correlate exceptions with service deployments directly in your Logz.io Exceptions tab.
  name: Logz.io Deployments API
  slug: logz-io-deployments-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: 'Drop filters provide a solution for filtering out logs before they are indexed in your account to help lower costs and reduce account volume. Drop filters evaluate logs for exact field:value matches. '
  name: Logz.io Drop filters API
  slug: logz-io-drop-filters-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana alerting provisioning API from Logz.io — 2 operation(s) for grafana alerting provisioning.
  name: Logz.io Grafana alerting provisioning API
  slug: logz-io-grafana-alerting-provisioning-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana annotations API from Logz.io — 5 operation(s) for grafana annotations.
  name: Logz.io Grafana annotations API
  slug: logz-io-grafana-annotations-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana contact points API from Logz.io — 3 operation(s) for grafana contact points.
  name: Logz.io Grafana contact points API
  slug: logz-io-grafana-contact-points-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana dashboard search API from Logz.io — 1 operation(s) for grafana dashboard search.
  name: Logz.io Grafana dashboard search API
  slug: logz-io-grafana-dashboard-search-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana dashboards API from Logz.io — 8 operation(s) for grafana dashboards.
  name: Logz.io Grafana dashboards API
  slug: logz-io-grafana-dashboards-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana data source API from Logz.io — 2 operation(s) for grafana data source.
  name: Logz.io Grafana data source API
  slug: logz-io-grafana-data-source-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana Folders API from Logz.io — 2 operation(s) for grafana folders.
  name: Logz.io Grafana Folders API
  slug: logz-io-grafana-folders-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana silence management API from Logz.io — 3 operation(s) for grafana silence management.
  name: Logz.io Grafana silence management API
  slug: logz-io-grafana-silence-management-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Grafana snapshots API from Logz.io — 4 operation(s) for grafana snapshots.
  name: Logz.io Grafana snapshots API
  slug: logz-io-grafana-snapshots-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Import or export Kibana objects API from Logz.io — 2 operation(s) for import or export kibana objects.
  name: Logz.io Import or export Kibana objects API
  slug: logz-io-import-or-export-kibana-objects-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: 'Logz.io monitors your logs for Insights to help you preempt issues and alert you of potential problems. There are two types of Insights: * LOGCEPTION - Application errors and exceptions identified in '
  name: Logz.io Insights API
  slug: logz-io-insights-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Label Values API from Logz.io — 1 operation(s) for label values.
  name: Logz.io Label Values API
  slug: logz-io-label-values-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Labels API from Logz.io — 1 operation(s) for labels.
  name: Logz.io Labels API
  slug: logz-io-labels-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Logz.io snapshots API from Logz.io — 2 operation(s) for logz.io snapshots.
  name: Logz.io Logz.io snapshots API
  slug: logz-io-logz-io-snapshots-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Lookup lists API from Logz.io — 7 operation(s) for lookup lists.
  name: Logz.io Lookup lists API
  slug: logz-io-lookup-lists-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: You can manage API tokens for sub accounts.
  name: Logz.io Manage API tokens API
  slug: logz-io-manage-api-tokens-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Use these API endpoints to create, update, retrieve, or delete log shipping tokens.
  name: Logz.io Manage log shipping tokens API
  slug: logz-io-manage-log-shipping-tokens-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Manage metrics account API from Logz.io — 2 operation(s) for manage metrics account.
  name: Logz.io Manage metrics account API
  slug: logz-io-manage-metrics-account-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Logz.io can send notifications to your preferred workspaces, such as Opsgenie, BigPanda, PagerDuty, and Slack. Notifications are typically sent when alerts are triggered, when a user shares a Kibana o
  name: Logz.io Manage notification endpoints API
  slug: logz-io-manage-notification-endpoints-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: You can share Kibana visualization and dashboard snapshots using shared tokens. Snapshots are stored for 30 days and automatically deleted afterwards. Token filters are available to help you control w
  name: Logz.io Manage shared tokens API
  slug: logz-io-manage-shared-tokens-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: 'Use these API requests to manage time-based log accounts: * Create, update, or delete a sub account. * Allocate daily capacity to the main account and/or sub accounts. * Retrieve account activity stat'
  name: Logz.io Manage time-based log accounts API
  slug: logz-io-manage-time-based-log-accounts-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Manage users API from Logz.io — 8 operation(s) for manage users.
  name: Logz.io Manage users API
  slug: logz-io-manage-users-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Parsing API from Logz.io — 3 operation(s) for parsing.
  name: Logz.io Parsing API
  slug: logz-io-parsing-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Query API from Logz.io — 1 operation(s) for query.
  name: Logz.io Query API
  slug: logz-io-query-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Range Query API from Logz.io — 1 operation(s) for range query.
  name: Logz.io Range Query API
  slug: logz-io-range-query-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: 'You can restore data from your active archiving account, whether an AWS S3 bucket or Azure Blob Storage. Restoring data gives you the option to query logs after they have expired from your time-based '
  name: Logz.io Restore logs API
  slug: logz-io-restore-logs-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Retrieve audit trail API from Logz.io — 2 operation(s) for retrieve audit trail.
  name: Logz.io Retrieve audit trail API
  slug: logz-io-retrieve-audit-trail-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Use the Elasticsearch Search API DSL query language to search your Logz.io data. To ensure system performance and data availability, we've introduced some limitations to the original Elasticsearch spe
  name: Logz.io Search logs API
  slug: logz-io-search-logs-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: A security account with SIEM allows you to use the SIEM platform. You can create a SIEM account using an API call.
  name: Logz.io Security account API
  slug: logz-io-security-account-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: A security event is logged whenever a security rule triggers in your [Logz.io Cloud SIEM account](https://app.logz.io/#/dashboard/security/rules/rule-definitions?from=0&sortBy=updatedAt&sortOrder=DESC
  name: Logz.io Security events API
  slug: logz-io-security-events-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: Security rules help you connect the dots between your data sources and events that could indicate a security threat or breach. Your Cloud SIEM account comes pre-configured with security rules for diff
  name: Logz.io Security rules API
  slug: logz-io-security-rules-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Time Series API from Logz.io — 1 operation(s) for time series.
  name: Logz.io Time Series API
  slug: logz-io-time-series-api
- baseURL: https://api.logz.io/v1/search
  baseurl_source: declared
  description: The Whoami API from Logz.io — 1 operation(s) for whoami.
  name: Logz.io Whoami API
  slug: logz-io-whoami-api
arazzos:
- description: Confirm which account a token belongs to, then list its associated accounts.
  name: Logz.io Verify Token And Discover Accounts
  slug: logz-io-account-verify-workflow
- description: Create an alert, refine its threshold, then list all alerts to confirm it.
  name: Logz.io Alert Create, Update, And List
  slug: logz-io-alert-create-update-list-workflow
- description: Create an alert, disable it for a maintenance window, re-enable it, and verify.
  name: Logz.io Alert Enable/Disable Lifecycle
  slug: logz-io-alert-lifecycle-workflow
- description: Create a custom webhook notification endpoint and an alert that routes to it.
  name: Logz.io Custom Webhook Endpoint Then Alert
  slug: logz-io-custom-endpoint-then-alert-workflow
- description: Create a Grafana folder, save a dashboard into it, and read it back by uid.
  name: Logz.io Grafana Dashboard In New Folder
  slug: logz-io-dashboard-in-folder-workflow
- description: List notification endpoints, confirm one by id, and delete it.
  name: Logz.io Notification Endpoint Cleanup
  slug: logz-io-endpoint-cleanup-workflow
- description: Create a Slack notification endpoint, then wire a new alert to notify it.
  name: Logz.io Notification Endpoint Then Alert
  slug: logz-io-endpoint-then-alert-workflow
- description: Create a Grafana contact point, confirm it by name, and list alert rules.
  name: Logz.io Grafana Contact Point Setup
  slug: logz-io-grafana-contact-point-workflow
- description: Discover label names, list matching series, then run an instant PromQL query.
  name: Logz.io Metrics Explore And Query
  slug: logz-io-metrics-explore-workflow
- description: Run a log search, then open a scroll to page through the full result set.
  name: Logz.io Search Then Scroll Logs
  slug: logz-io-search-then-scroll-workflow
- description: List sub accounts, fetch one by id to confirm, and delete it.
  name: Logz.io Sub Account Cleanup
  slug: logz-io-subaccount-cleanup-workflow
- description: Create a time-based log sub account, read it back, and adjust its retention.
  name: Logz.io Provision a Sub Account
  slug: logz-io-subaccount-provision-workflow
- description: Find an alert by title and update it if it exists, otherwise create it.
  name: Logz.io Upsert an Alert
  slug: logz-io-upsert-alert-workflow
artifact_total: 82
common:
- group: company
  title: ''
  type: Website
  url: https://www.logz.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/security/logz-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/logz-io-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/security/logz-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logz-io-domain-security.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/logzio/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-account-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-account-verify-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-alert-create-update-list-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-alert-create-update-list-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-alert-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-alert-lifecycle-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-custom-endpoint-then-alert-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-custom-endpoint-then-alert-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-dashboard-in-folder-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-dashboard-in-folder-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-endpoint-cleanup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-endpoint-cleanup-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-endpoint-then-alert-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-endpoint-then-alert-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-grafana-contact-point-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-grafana-contact-point-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-metrics-explore-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-metrics-explore-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-search-then-scroll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-search-then-scroll-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-subaccount-cleanup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-subaccount-cleanup-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-subaccount-provision-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-subaccount-provision-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/arazzo/logz-io-upsert-alert-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/logz-io-upsert-alert-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://logz.io/
- group: start
  title: ''
  type: Login
  url: https://app.logz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logz.io/api/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.logz.io/docs/logz/logz-io-api
- group: auth
  title: ''
  type: Authentication
  url: https://app.logz.io/#/dashboard/settings/manage-tokens/api
- group: other
  title: ''
  type: Regions
  url: https://docs.logz.io/user-guide/accounts/account-region.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.logz.io/user-guide/giveittome/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://logz.io/about-us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://logz.io/about-us/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://logz.io/learn/security-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://logz.io/trust-center/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.logz.io/
- group: company
  title: ''
  type: Blog
  url: https://logz.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://logz.io/blog/category/news/
- group: operate
  title: ''
  type: Support
  url: https://logz.io/support/
- group: operate
  title: ''
  type: Support
  url: https://docs.logz.io/contact-support.html
- group: operate
  title: ''
  type: ContactUs
  url: https://logz.io/about/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logzio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logz.io/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/logzio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCRtxh4MS8gWQ8mTCnTcLZ-Q
- group: company
  title: ''
  type: Careers
  url: https://logz.io/about-us/careers/
- group: company
  title: ''
  type: AboutUs
  url: https://logz.io/about-us/
- group: commercial
  title: ''
  type: License
  url: https://logz.io/about-us/forked-statement/
- group: other
  title: ''
  type: CaseStudies
  url: https://logz.io/customers/
- group: company
  title: ''
  type: Partners
  url: https://logz.io/partners/
- group: other
  title: ''
  type: Events
  url: https://logz.io/events/
- group: other
  title: ''
  type: Containers
  url: https://hub.docker.com/u/logzio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logz.io/integrations/terraform/
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/terraform-provider-logzio
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio_terraform_client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-browser
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-java-sender
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-python-handler
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-bunyan
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-log4j2-appender
- group: build
  title: ''
  type: SDKs
  url: https://github.com/logzio/logzio-logback-appender
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio-helm
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio-k8s
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio_aws_serverless
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/logzio-azure-serverless
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/grafana-logzio-datasource
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/docker-collector-logs
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/docker-collector-metrics
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/docker-logging-plugin
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/fluent-bit-logzio-output
- group: build
  title: ''
  type: Tools
  url: https://github.com/logzio/sawmill
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/logzio/logz-docs
- group: operate
  title: ''
  type: Community
  url: https://github.com/logzio/community
- group: learn
  title: ''
  type: Learning
  url: https://logz.io/learn/complete-guide-elk-stack/
- group: learn
  title: ''
  type: Learning
  url: https://logz.io/learn/
- group: commercial
  title: ''
  type: Plans
  url: https://logz.io/pricing/
- group: commercial
  title: ''
  type: Pricing
  url: https://logz.io/pricing/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/openapi/_original/logz-io-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/logz-io-api-openapi.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/plans/logz-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logz-io-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/rate-limits/logz-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/logz-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/finops/logz-io-finops.yml
  title: ''
  type: FinOps
  url: finops/logz-io-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/json-ld/logz-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/logz-io-context.jsonld
created: '2026-05-25'
description: Logz.io is a managed cloud observability platform built on the ELK Stack (Elasticsearch / Logstash / Kibana, plus OpenSearch and Grafana) that unifies log management, infrastructure monitoring, distributed tracing, and Cloud SIEM behind a consumption-based pricing model. The platform pairs an AI Agent layer for root-cause analysis with native OpenTelemetry, Prometheus, Grafana, and Perses compatibility, and exposes its entire control plane through a single OpenAPI 2.0-described public API covering search, alerting, sub-account management, security rules, parsing pipelines, archive / restore, and visualization-as-code via the Logz.io fork of Grafana and Perses.
finops:
- name: Logz Io Finops
  service_category: Management and Governance
  slug: logz-io-finops
graphqls:
- description: Conceptual GraphQL schema for the Logz.io cloud observability platform. Logz.io unifies log management, infrastructure metrics, distributed tracing, and Cloud SIEM behind a single API surface. This sc
  name: Logz.io GraphQL Schema
  slug: logz-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logz-io.png
json_schemas:
- name: Logz.io Alert Rule
  property_count: 10
  slug: logz-io-alert-rule
- name: Logz.io Log Document
  property_count: 16
  slug: logz-io-log-document
- name: Logz.io Metric Sample
  property_count: 3
  slug: logz-io-metric-sample
- name: Logz.io Search Request
  property_count: 8
  slug: logz-io-search-request
jsonld:
- class_count: 0
  name: Logz Io Context
  property_count: 40
  slug: logz-io-context
layout: provider
modified: '2026-09-16'
name: Logz.io
nav: Providers
network: true
overview: 'Logz.io publishes 57 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Archive logs API, Associated accounts API, and 54 more. Tagged areas include Observability, Logging, Metrics, Tracing, and SIEM.


  The Logz.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Logz.io''s developer surface includes developer portal, documentation, authentication, getting-started guide, engineering blog, changelog, support, and 73 more developer resources.'
plans:
- name: Logz Io Plans Pricing
  plan_count: 7
  slug: logz-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Logz Io Rate Limits
  slug: logz-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Logz.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: logz-io-jsonschema-spectral-rules
score:
  band: strong
  composite: 66.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 78.3
    catalog_earned_first_party: 0.0
    catalog_gap: 36.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 92.1
    contract_governance: 9.8
    contract_quality: 66.1
    developer_ergonomics: 71.4
    discoverability: 63.0
    operational_transparency: 68.4
  previous_composite: 64.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 57
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/logz-io/refs/heads/main/screenshots/logz-io-2026-06-20T184702.png
security:
- kind: domain-security
  name: Logz Io Domain Security
  slug: logz-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Logz Io Trust Center
  slug: logz-io-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP
slug: logz-io
tags:
- Observability
- Logging
- Metrics
- Tracing
- SIEM
- ELK
- Elasticsearch
- OpenSearch
- Prometheus
- Grafana
- OpenTelemetry
- AIOps
- Cloud Observability
- Managed ELK
- Cost Management
website: https://www.logz.io/
---
