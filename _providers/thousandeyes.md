---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-10-04'
api_count: 53
apis:
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Account group CRUD operations
  name: ThousandEyes Account Groups API
  phrasing_intents:
  - id: getAccountGroups
    intent: List account groups
    question: Which account groups can I access?
  - id: createAccountGroup
    intent: Create an account group
    question: What permission is needed to create a new account group?
  - id: getAccountGroup
    intent: Get an account group's details
    question: What details can I see for one account group?
  - id: updateAccountGroup
    intent: Rename an account group or change its agents
    question: Can I rename an existing account group?
  - id: deleteAccountGroup
    intent: Delete an account group
    question: Which permissions are required to delete an account group?
  phrasing_ops: 5
  slug: thousandeyes-account-groups-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Agent Proxies API from ThousandEyes — 1 operation(s) for agent proxies.
  name: ThousandEyes Agent Proxies API
  phrasing_intents:
  - id: getAgentsProxies
    intent: List Enterprise Agent proxies
    question: Which proxies are configured for our Enterprise Agents?
  phrasing_ops: 1
  slug: thousandeyes-agent-proxies-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Agent to Agent Instant Tests API from ThousandEyes — 1 operation(s) for agent to agent instant tests.
  name: ThousandEyes Agent to Agent Instant Tests API
  phrasing_intents:
  - id: createAgentToAgentInstantTest
    intent: Run an agent-to-agent instant test
    question: Can I run a one-off network test between two of my agents right now?
  phrasing_ops: 1
  slug: thousandeyes-agent-to-agent-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Agent to Agent test management operations
  name: ThousandEyes Agent to Agent Tests API
  phrasing_intents:
  - id: getAgentToAgentTests
    intent: List Agent to Agent tests
    question: What Agent to Agent tests are set up in my account?
  - id: createAgentToAgentTest
    intent: Create an Agent to Agent test
    question: How do I measure network performance between two of my agents?
  - id: getAgentToAgentTest
    intent: Get an Agent to Agent test
    question: How do I see the interval, targets and agents of an Agent to Agent test?
  - id: updateAgentToAgentTest
    intent: Update an Agent to Agent test
    question: What can I change on a shared Agent to Agent test?
  - id: deleteAgentToAgentTest
    intent: Delete an Agent to Agent test
    question: Can I delete an Agent to Agent test?
  phrasing_ops: 5
  slug: thousandeyes-agent-to-agent-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Agent To Server Endpoint Dynamic Tests API from ThousandEyes — 2 operation(s) for agent to server endpoint dynamic tests.
  name: ThousandEyes Agent To Server Endpoint Dynamic Tests API
  phrasing_intents:
  - id: getAgentToServerEndpointDynamicTests
    intent: List endpoint dynamic tests
    question: Which agent-to-server dynamic tests run from our endpoint agents?
  - id: createAgentToServerEndpointDynamicTest
    intent: Create an endpoint dynamic test
    question: Can I have endpoint agents dynamically test the path to an application like Teams?
  - id: getAgentToServerEndpointDynamicTest
    intent: Get an endpoint dynamic test
    question: What interval and targets are set on one endpoint dynamic test?
  - id: updateAgentToServerEndpointDynamicTest
    intent: Update or toggle an endpoint dynamic test
    question: Can I disable an endpoint dynamic test without deleting it?
  - id: deleteAgentToServerEndpointDynamicTest
    intent: Delete an endpoint dynamic test
    question: Can I remove an agent-to-server dynamic test from our endpoint agents?
  phrasing_ops: 5
  slug: thousandeyes-agent-to-server-endpoint-dynamic-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Agent to Server Endpoint Instant Scheduled Tests API from ThousandEyes — 1 operation(s) for agent to server endpoint instant scheduled tests.
  name: ThousandEyes Agent to Server Endpoint Instant Scheduled Tests API
  phrasing_intents:
  - id: createAgentToServerScheduledInstantTest
    intent: Run an instant agent to server endpoint test
    question: Can I run a one-off network test from endpoint agents to a server right now?
  phrasing_ops: 1
  slug: thousandeyes-agent-to-server-endpoint-instant-scheduled-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Agent to Server Endpoint Scheduled Tests API from ThousandEyes — 2 operation(s) for agent to server endpoint scheduled tests.
  name: ThousandEyes Agent to Server Endpoint Scheduled Tests API
  phrasing_intents:
  - id: getAgentToServerEndpointScheduledTests
    intent: List agent to server endpoint tests
    question: Which agent to server tests are scheduled on my endpoint agents?
  - id: createAgentToServerEndpointScheduledTest
    intent: Create an agent to server endpoint test
    question: How do I schedule a network test from employee laptops to a server?
  - id: getAgentToServerEndpointScheduledTest
    intent: Get an agent to server endpoint test
    question: Where do I see the settings of one endpoint agent-to-server test?
  - id: updateAgentToServerEndpointScheduledTest
    intent: Update an agent to server endpoint test
    question: Can I disable an endpoint agent-to-server test without deleting it?
  - id: deleteAgentToServerEndpointScheduledTest
    intent: Delete an agent to server endpoint test
    question: Can I remove an agent to server test from my endpoint agents?
  phrasing_ops: 5
  slug: thousandeyes-agent-to-server-endpoint-scheduled-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Agent to Server Instant Tests API from ThousandEyes — 1 operation(s) for agent to server instant tests.
  name: ThousandEyes Agent to Server Instant Tests API
  phrasing_intents:
  - id: createAgentToServerInstantTest
    intent: Run an agent-to-server instant test
    question: Can I run a one-time network test from agents to a server right now?
  phrasing_ops: 1
  slug: thousandeyes-agent-to-server-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Agent to Server test management operations
  name: ThousandEyes Agent to Server Tests API
  phrasing_intents:
  - id: getAgentToServerTests
    intent: List Agent to Server tests
    question: Which Agent to Server network tests are configured?
  - id: createAgentToServerTest
    intent: Create an Agent to Server test
    question: What permissions do I need to create an Agent to Server test?
  - id: getAgentToServerTest
    intent: Get an Agent to Server test
    question: Which agents and alert rules are on a given Agent to Server test?
  - id: updateAgentToServerTest
    intent: Update an Agent to Server test
    question: What can I change on a shared Agent to Server test?
  - id: deleteAgentToServerTest
    intent: Delete an Agent to Server test
    question: Can I delete an Agent to Server test I no longer need?
  phrasing_ops: 5
  slug: thousandeyes-agent-to-server-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Alert Rules API from ThousandEyes — 2 operation(s) for alert rules.
  name: ThousandEyes Alert Rules API
  phrasing_intents:
  - id: getAlertsRules
    intent: List alert rules
    question: What alert rules exist in my ThousandEyes account?
  - id: createAlertRule
    intent: Create an alert rule
    question: How do I alert when packet loss crosses a threshold?
  - id: getAlertRule
    intent: Get an alert rule
    question: What conditions does one alert rule check?
  - id: updateAlertRule
    intent: Update an alert rule
    question: How do I change the threshold of an existing alert rule?
  - id: deleteAlertRule
    intent: Delete an alert rule
    question: How do I delete an alert rule that is linked to tests?
  phrasing_ops: 5
  slug: thousandeyes-alert-rules-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Alert Suppression Windows API from ThousandEyes — 2 operation(s) for alert suppression windows.
  name: ThousandEyes Alert Suppression Windows API
  phrasing_intents:
  - id: getAlertSuppressionWindows
    intent: List alert suppression windows
    question: Which alert suppression windows are set up for maintenance?
  - id: createAlertSuppressionWindow
    intent: Create an alert suppression window
    question: Can I silence alerts for certain tests during a maintenance window?
  - id: getAlertSuppressionWindow
    intent: Get an alert suppression window
    question: What tests and schedule does a specific suppression window cover?
  - id: updateAlertSuppressionWindow
    intent: Update an alert suppression window
    question: Can I extend an existing maintenance window?
  - id: deleteAlertSuppressionWindow
    intent: Delete an alert suppression window
    question: Can I remove a suppression window once maintenance is over?
  phrasing_ops: 5
  slug: thousandeyes-alert-suppression-windows-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Alerts API from ThousandEyes — 2 operation(s) for alerts.
  name: ThousandEyes Alerts API
  phrasing_intents:
  - id: getAlerts
    intent: List alerts
    question: Which alerts are currently triggered?
  - id: getAlert
    intent: Get an alert's details
    question: What triggered a specific alert?
  phrasing_ops: 2
  slug: thousandeyes-alerts-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The API Instant Tests API from ThousandEyes — 1 operation(s) for api instant tests.
  name: ThousandEyes API Instant Tests API
  phrasing_intents:
  - id: createApiInstantTest
    intent: Run an instant API test
    question: Can I run a one-time API test right now instead of scheduling it?
  phrasing_ops: 1
  slug: thousandeyes-api-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The API Test Results API from ThousandEyes — 2 operation(s) for api test results.
  name: ThousandEyes API Test Results API
  phrasing_intents:
  - id: getTestApiResults
    intent: Get API test results
    question: Did my API test's requests succeed in the most recent round?
  - id: getTestApiAgentRoundResults
    intent: Get API test results for an agent round
    question: How do I see what one agent got back in a single API test round?
  phrasing_ops: 2
  slug: thousandeyes-api-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: API test management operations
  name: ThousandEyes API Tests API
  phrasing_intents:
  - id: getApiTests
    intent: List API tests
    question: What API tests do I have configured?
  - id: createApiTest
    intent: Create an API test
    question: How do I set up a scheduled test that calls my API endpoints?
  - id: getApiTest
    intent: Get an API test
    question: Can I see the alert rules and agents attached to an API test?
  - id: updateApiTest
    intent: Update an API test
    question: Which fields can I change on a shared API test?
  - id: deleteApiTest
    intent: Delete an API test
    question: Is there a way to remove an API test?
  phrasing_ops: 5
  slug: thousandeyes-api-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The API Token API from ThousandEyes — 1 operation(s) for api token.
  name: ThousandEyes API Token API
  phrasing_intents:
  - id: regenerateApiToken
    intent: Regenerate my API bearer token
    question: Can I rotate my ThousandEyes API bearer token?
  phrasing_ops: 1
  slug: thousandeyes-api-token-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Autonomous System Prefixes API from ThousandEyes — 1 operation(s) for autonomous system prefixes.
  name: ThousandEyes Autonomous System Prefixes API
  phrasing_intents:
  - id: getAutonomousSystemAssociatedPrefixes
    intent: List prefixes for an autonomous system
    question: Which IP prefixes does a given ASN announce?
  phrasing_ops: 1
  slug: thousandeyes-autonomous-system-prefixes-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The BGP monitors API from ThousandEyes — 1 operation(s) for bgp monitors.
  name: ThousandEyes BGP monitors API
  phrasing_intents:
  - id: getBgpMonitors
    intent: List BGP monitors
    question: Which BGP monitors, public and private, are available to me?
  phrasing_ops: 1
  slug: thousandeyes-bgp-monitors-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: BGP test management operations
  name: ThousandEyes BGP Tests API
  phrasing_intents:
  - id: getBgpTests
    intent: List BGP tests
    question: Which BGP tests are monitoring our prefixes?
  - id: createBgpTest
    intent: Create a BGP test
    question: Can I monitor route changes for one of our prefixes?
  - id: getBgpTest
    intent: Get a BGP test
    question: What alert rules and monitors does a specific BGP test use?
  - id: updateBgpTest
    intent: Update a BGP test
    question: Can I change the monitors on an existing BGP test?
  - id: deleteBgpTest
    intent: Delete a BGP test
    question: Can I stop and remove a BGP test?
  phrasing_ops: 5
  slug: thousandeyes-bgp-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Cloud and Enterprise Agent Notification Rules API from ThousandEyes — 2 operation(s) for cloud and enterprise agent notification rules.
  name: ThousandEyes Cloud and Enterprise Agent Notification Rules API
  phrasing_intents:
  - id: getAgentsNotificationRules
    intent: List agent notification rules
    question: Which agent notification rules are configured in my account?
  - id: getAgentsNotificationRule
    intent: Get an agent notification rule
    question: Which agents is a particular notification rule assigned to?
  phrasing_ops: 2
  slug: thousandeyes-cloud-and-enterprise-agent-notification-rules-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Cloud and Enterprise Agents API from ThousandEyes — 2 operation(s) for cloud and enterprise agents.
  name: ThousandEyes Cloud and Enterprise Agents API
  phrasing_intents:
  - id: getAgents
    intent: List Cloud and Enterprise Agents
    question: Which Cloud and Enterprise Agents can my tests run from?
  - id: getAgent
    intent: Get a Cloud or Enterprise Agent
    question: What tests are assigned to a particular agent?
  - id: updateAgent
    intent: Update an Enterprise Agent
    question: Can I rename an Enterprise Agent or disable it?
  - id: deleteAgent
    intent: Delete an Enterprise Agent
    question: What happens to tests when an Enterprise Agent is deleted?
  phrasing_ops: 4
  slug: thousandeyes-cloud-and-enterprise-agents-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Manage Cloud Insights integration policy settings for AWS and Azure.
  name: ThousandEyes Cloud Insights Integration Policy Settings API
  phrasing_intents:
  - id: getAWSIntegrationPolicySettings
    intent: Get AWS integration policy settings
    question: Which AWS regions and resource types am I inventorying?
  - id: updateAWSIntegrationPolicySettings
    intent: Update AWS integration policy settings
    question: How do I limit AWS inventory to certain regions?
  - id: getAzureIntegrationPolicySettings
    intent: Get Azure integration policy settings
    question: Which Azure resource group types are being monitored?
  - id: updateAzureIntegrationPolicySettings
    intent: Update Azure integration policy settings
    question: How do I exclude certain Azure subscriptions from inventory?
  phrasing_ops: 4
  slug: thousandeyes-cloud-insights-integration-policy-settings-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Manage Cloud Insights integrations for AWS and Azure.
  name: ThousandEyes Cloud Insights Integrations API
  phrasing_intents:
  - id: getAllAWSMonitoringIntegrations
    intent: List AWS monitoring integrations
    question: Which AWS accounts have I connected to ThousandEyes Cloud Insights?
  - id: getAWSMonitoringIntegration
    intent: Get an AWS monitoring integration
    question: Where can I check the configuration of one specific AWS integration?
  - id: deleteAwsMonitoringIntegration
    intent: Delete an AWS monitoring integration
    question: How do I disconnect an AWS account from Cloud Insights?
  - id: createAWSInventoryMonitoringIntegration
    intent: Connect AWS inventory monitoring
    question: How do I start monitoring my AWS resource inventory?
  - id: createAWSFlowLogsMonitoringIntegration
    intent: Connect AWS flow logs monitoring
    question: How do I send AWS VPC flow logs into Cloud Insights?
  - id: getAWSInventoryMonitoringIntegrationPolicies
    intent: Get IAM policies for AWS inventory
    question: What IAM permissions does the AWS inventory integration require?
  - id: getAWSFlowlogsMonitoringIntegrationPolicies
    intent: Get IAM policies for AWS flow logs
    question: What IAM policy do I attach so flow logs can be read?
  - id: getAllAzureMonitoringIntegrations
    intent: List Azure monitoring integrations
    question: Which Azure tenants are connected to Cloud Insights?
  phrasing_ops: 14
  slug: thousandeyes-cloud-insights-integrations-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Credential Vault operations allow you to configure vault secrets.
  name: ThousandEyes Credential Vault Operations API
  phrasing_intents:
  - id: getCredentialVaultOperation
    intent: Get a Credential Vault operation
    question: Can I look up a single Credential Vault operation by ID?
  - id: updateCredentialVaultOperation
    intent: Update a Credential Vault operation
    question: How do I change the secrets on an existing Credential Vault operation?
  - id: deleteCredentialVaultOperation
    intent: Delete a Credential Vault operation
    question: Will deleting a Credential Vault operation disable tests that depend on it?
  - id: getCredentialVaultOperations
    intent: List Credential Vault operations
    question: Which Credential Vault operations exist in my account group?
  - id: createCredentialVaultOperation
    intent: Create a Credential Vault operation
    question: How do I create an operation that pulls secrets from a credential vault?
  phrasing_ops: 5
  slug: thousandeyes-credential-vault-operations-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Credentials API from ThousandEyes — 2 operation(s) for credentials.
  name: ThousandEyes Credentials API
  phrasing_intents:
  - id: getCredentials
    intent: List transaction test credentials
    question: Which stored credentials can my transaction tests use?
  - id: createCredential
    intent: Create a transaction test credential
    question: Can I store a password for web transaction scripts to use?
  - id: getCredential
    intent: Get a transaction test credential
    question: Can I view the details of one stored credential?
  - id: updateCredential
    intent: Update a transaction test credential
    question: Can I rotate the secret stored in an existing credential?
  - id: deleteCredential
    intent: Delete a transaction test credential
    question: Can I delete a credential that transaction tests no longer use?
  phrasing_ops: 5
  slug: thousandeyes-credentials-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The CyberArk Conjur instance you want the ThousandEyes platform to integrate with.
  name: ThousandEyes CyberArk Conjur Connectors API
  phrasing_intents:
  - id: getConjurConnector
    intent: Get a CyberArk Conjur connector
    question: What is configured on one of my CyberArk Conjur connectors?
  - id: updateConjurConnector
    intent: Update a CyberArk Conjur connector
    question: Can I change the Conjur target URL or credentials on an existing connector?
  - id: deleteConjurConnector
    intent: Delete a CyberArk Conjur connector
    question: Will deleting a Conjur connector disable any tests that use it?
  - id: getConjurConnectorOperations
    intent: List operations assigned to a Conjur connector
    question: Which operations are using a given Conjur connector?
  - id: setConjurConnectorOperations
    intent: Assign operations to a Conjur connector
    question: Does assigning operations to a Conjur connector replace the old assignments?
  - id: getConjurConnectors
    intent: List CyberArk Conjur connectors
    question: Which CyberArk Conjur connectors are set up in my account group?
  - id: createConjurConnector
    intent: Create a CyberArk Conjur connector
    question: Can I pull test secrets from CyberArk Conjur into ThousandEyes?
  phrasing_ops: 7
  slug: thousandeyes-cyberark-conjur-connectors-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Dashboard Snapshots CRUD operations
  name: ThousandEyes Dashboard Snapshots API
  phrasing_intents:
  - id: getDashboardSnapshots
    intent: List dashboard snapshots
    question: What dashboard snapshots exist in my account group?
  - id: createDashboardSnapshot
    intent: Create a dashboard snapshot
    question: How do I freeze a dashboard for a time range to share it?
  - id: getDashboardSnapshot
    intent: Get a dashboard snapshot's widgets
    question: Which widgets does a dashboard snapshot contain?
  - id: updateDashboardSnapshotExpirationDate
    intent: Change a dashboard snapshot's expiry
    question: How do I extend when a dashboard snapshot expires?
  - id: deleteDashboardSnapshot
    intent: Delete a dashboard snapshot
    question: Can I delete a dashboard snapshot I shared?
  - id: getDashboardSnapshotWidgetData
    intent: Get data behind a snapshot widget
    question: How do I pull the raw metrics behind one widget in a dashboard snapshot?
  phrasing_ops: 6
  slug: thousandeyes-dashboard-snapshots-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Dashboards and Widgets operations
  name: ThousandEyes Dashboards API
  phrasing_intents:
  - id: getDashboards
    intent: List dashboards in an account group
    question: Which dashboards exist in my ThousandEyes account group?
  - id: createDashboard
    intent: Create a new dashboard
    question: What permissions do I need to build a brand-new dashboard?
  - id: getDashboard
    intent: Get a dashboard and its widgets
    question: What widgets are on a particular dashboard?
  - id: updateDashboard
    intent: Update an existing dashboard
    question: Can I rename a dashboard or change its widgets after it's built?
  - id: deleteDashboard
    intent: Delete a dashboard
    question: Can I permanently remove a dashboard I no longer use?
  - id: cloneDashboard
    intent: Clone a dashboard into a copy
    question: Can I copy an existing dashboard instead of rebuilding its widgets?
  - id: updateDashboardSchedule
    intent: Schedule dashboard snapshots
    question: Can I have snapshots of a dashboard generated on a recurring schedule?
  - id: deleteDashboardSchedule
    intent: Remove a dashboard's snapshot schedule
    question: Can I stop recurring snapshots of a dashboard without losing the old ones?
  phrasing_ops: 11
  slug: thousandeyes-dashboards-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Dashboards Filters API from ThousandEyes — 2 operation(s) for dashboards filters.
  name: ThousandEyes Dashboards Filters API
  phrasing_intents:
  - id: getDashboardsFilters
    intent: List dashboard filters
    question: What saved dashboard filters are in my account group?
  - id: createDashboardFilter
    intent: Create a dashboard filter
    question: How do I save a reusable filter for my dashboards?
  - id: getDashboardFilter
    intent: Get a dashboard filter
    question: What data source filters are inside one dashboard filter?
  - id: updateDashboardFilter
    intent: Update a dashboard filter
    question: Can I edit a dashboard filter someone else created?
  - id: deleteDashboardFilter
    intent: Delete a dashboard filter
    question: Who is allowed to delete a dashboard filter?
  phrasing_ops: 5
  slug: thousandeyes-dashboards-filters-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The DNS Server Instant Tests API from ThousandEyes — 1 operation(s) for dns server instant tests.
  name: ThousandEyes DNS Server Instant Tests API
  phrasing_intents:
  - id: createDnsServerInstantTest
    intent: Run an instant DNS server test
    question: Can I check right now how my DNS servers resolve a domain?
  phrasing_ops: 1
  slug: thousandeyes-dns-server-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The DNS Server Test Results API from ThousandEyes — 2 operation(s) for dns server test results.
  name: ThousandEyes DNS Server Test Results API
  phrasing_intents:
  - id: getTestDnsServerResult
    intent: Get DNS results for one server
    question: What did one specific DNS server resolve during my test?
  - id: getTestDnsServersResults
    intent: Get DNS server test results
    question: How do I see DNS mappings and resolution times across all servers in a test?
  phrasing_ops: 2
  slug: thousandeyes-dns-server-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: DNS Server test management operations
  name: ThousandEyes DNS Server Tests API
  phrasing_intents:
  - id: getDnsServerTests
    intent: List DNS Server tests
    question: Which DNS Server tests are checking our name servers?
  - id: createDnsServerTest
    intent: Create a DNS Server test
    question: Can I monitor whether our authoritative DNS servers answer correctly?
  - id: getDnsServerTest
    intent: Get a DNS Server test
    question: What servers and agents does one DNS Server test use?
  - id: updateDnsServerTest
    intent: Update a DNS Server test
    question: Can I change the BGP monitors on a DNS Server test?
  - id: deleteDnsServerTest
    intent: Delete a DNS Server test
    question: Can I remove a DNS Server test?
  phrasing_ops: 5
  slug: thousandeyes-dns-server-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The DNS Trace Instant Tests API from ThousandEyes — 1 operation(s) for dns trace instant tests.
  name: ThousandEyes DNS Trace Instant Tests API
  phrasing_intents:
  - id: createDnsTraceInstantTest
    intent: Run a DNS trace instant test
    question: Can I trace DNS resolution for a domain on demand?
  phrasing_ops: 1
  slug: thousandeyes-dns-trace-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The DNS Trace Test Results API from ThousandEyes — 1 operation(s) for dns trace test results.
  name: ThousandEyes DNS Trace Test Results API
  phrasing_intents:
  - id: getTestDnsTraceResults
    intent: Get DNS trace test results
    question: What did the DNS delegation chain look like in my trace test?
  phrasing_ops: 1
  slug: thousandeyes-dns-trace-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: DNS Trace test management operations
  name: ThousandEyes DNS Trace Tests API
  phrasing_intents:
  - id: getDnsTraceTests
    intent: List DNS Trace tests
    question: What DNS Trace tests am I running?
  - id: createDnsTraceTest
    intent: Create a DNS Trace test
    question: How do I trace DNS delegation for a domain on a schedule?
  - id: getDnsTraceTest
    intent: Get a DNS Trace test
    question: Which agents and interval does a DNS Trace test use?
  - id: updateDnsTraceTest
    intent: Update a DNS Trace test
    question: What can I change on a shared DNS Trace test?
  - id: deleteDnsTraceTest
    intent: Delete a DNS Trace test
    question: How do I delete a DNS Trace test?
  phrasing_ops: 5
  slug: thousandeyes-dns-trace-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The DNSSEC Instant Tests API from ThousandEyes — 1 operation(s) for dnssec instant tests.
  name: ThousandEyes DNSSEC Instant Tests API
  phrasing_intents:
  - id: createDnsSecInstantTest
    intent: Run a DNSSEC instant test
    question: Can I check a domain's DNSSEC validity on demand?
  phrasing_ops: 1
  slug: thousandeyes-dnssec-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The DNSSEC Test Results API from ThousandEyes — 1 operation(s) for dnssec test results.
  name: ThousandEyes DNSSEC Test Results API
  phrasing_intents:
  - id: getTestDnsSecResults
    intent: Get DNSSEC test results
    question: Is the DNSSEC key chain for my domain valid?
  phrasing_ops: 1
  slug: thousandeyes-dnssec-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: DNSSEC test management operations
  name: ThousandEyes DNSSEC Tests API
  phrasing_intents:
  - id: getDnsSecTests
    intent: List DNSSEC tests
    question: Which DNSSEC validation tests are configured?
  - id: createDnsSecTest
    intent: Create a DNSSEC test
    question: Can I continuously validate the DNSSEC chain of trust for a domain?
  - id: getDnsSecTest
    intent: Get a DNSSEC test
    question: What agents and alert rules are on a DNSSEC test?
  - id: updateDnsSecTest
    intent: Update a DNSSEC test
    question: Can I edit the alert settings of an existing DNSSEC test?
  - id: deleteDnsSecTest
    intent: Delete a DNSSEC test
    question: Can I delete a DNSSEC test?
  phrasing_ops: 5
  slug: thousandeyes-dnssec-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Emulation API from ThousandEyes — 2 operation(s) for emulation.
  name: ThousandEyes Emulation API
  phrasing_intents:
  - id: getUserAgents
    intent: List user-agent strings
    question: Which user-agent strings can browser tests emulate?
  - id: getEmulatedDevices
    intent: List emulated devices
    question: Which devices can browser tests emulate?
  - id: createEmulatedDevice
    intent: Create an emulated device
    question: Can I add a custom device size for browser tests to emulate?
  phrasing_ops: 3
  slug: thousandeyes-emulation-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Endpoint Agent Labels API from ThousandEyes — 2 operation(s) for endpoint agent labels.
  name: ThousandEyes Endpoint Agent Labels API
  phrasing_intents:
  - id: getEndpointLabels
    intent: List endpoint agent labels
    question: What labels group my endpoint agents?
  - id: createEndpointLabel
    intent: Create an endpoint agent label
    question: How do I group endpoint agents automatically with a label?
  - id: getEndpointLabel
    intent: Get an endpoint agent label
    question: What filters define a particular endpoint label?
  - id: updateEndpointLabel
    intent: Update an endpoint agent label
    question: How do I change the filters on an endpoint label?
  - id: deleteEndpointLabel
    intent: Delete an endpoint agent label
    question: Is there a way to delete an endpoint agent label?
  phrasing_ops: 5
  slug: thousandeyes-endpoint-agent-labels-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Endpoint Agent Log Items API from ThousandEyes — 1 operation(s) for endpoint agent log items.
  name: ThousandEyes Endpoint Agent Log Items API
  phrasing_intents:
  - id: getEndpointAgentLogItems
    intent: Get an endpoint agent's logs
    question: Can I pull the logs of a specific endpoint agent?
  phrasing_ops: 1
  slug: thousandeyes-endpoint-agent-log-items-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Endpoint Agents API from ThousandEyes — 6 operation(s) for endpoint agents.
  name: ThousandEyes Endpoint Agents API
  phrasing_intents:
  - id: getEndpointAgents
    intent: List endpoint agents
    question: Which endpoint agents are installed in my account group?
  - id: getEndpointAgent
    intent: Get an endpoint agent's details
    question: What details are recorded for a single endpoint agent?
  - id: updateEndpointAgent
    intent: Rename or relicense an endpoint agent
    question: Which endpoint agent fields can be changed after install?
  - id: deleteEndpointAgent
    intent: Delete an endpoint agent
    question: Can I remove an endpoint agent from a laptop we've retired?
  - id: filterEndpointAgents
    intent: Search endpoint agents by filters
    question: Can I search endpoint agents with multiple filter criteria and sorting?
  - id: getEndpointAgentsConnectionString
    intent: Get the endpoint agent connection string
    question: Where do I get the connection string to register new endpoint agents?
  - id: enableEndpointAgent
    intent: Enable an endpoint agent
    question: Can I turn a disabled endpoint agent back on?
  - id: disableEndpointAgent
    intent: Disable an endpoint agent
    question: Can I pause an endpoint agent without deleting it?
  phrasing_ops: 8
  slug: thousandeyes-endpoint-agents-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Endpoint Agents Transfer API from ThousandEyes — 2 operation(s) for endpoint agents transfer.
  name: ThousandEyes Endpoint Agents Transfer API
  phrasing_intents:
  - id: transferEndpointAgent
    intent: Transfer an endpoint agent to another account
    question: Can I move an endpoint agent to a different account group?
  - id: transferEndpointAgents
    intent: Bulk transfer endpoint agents
    question: Can I move many endpoint agents between accounts at once?
  phrasing_ops: 2
  slug: thousandeyes-endpoint-agents-transfer-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Endpoint Proxies API from ThousandEyes — 1 operation(s) for endpoint proxies.
  name: ThousandEyes Endpoint Proxies API
  phrasing_intents:
  - id: getEndpointProxies
    intent: List endpoint agent proxy settings
    question: What proxy settings are my endpoint agents using?
  phrasing_ops: 1
  slug: thousandeyes-endpoint-proxies-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Endpoint Real User Tests API from ThousandEyes — 1 operation(s) for endpoint real user tests.
  name: ThousandEyes Endpoint Real User Tests API
  phrasing_intents:
  - id: getEndpointRealUserTests
    intent: List endpoint real user tests
    question: Which domains are monitored by endpoint real user tests?
  phrasing_ops: 1
  slug: thousandeyes-endpoint-real-user-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Endpoint Scheduled Tests API from ThousandEyes — 1 operation(s) for endpoint scheduled tests.
  name: ThousandEyes Endpoint Scheduled Tests API
  phrasing_intents:
  - id: getEndpointScheduledTests
    intent: List all endpoint scheduled tests
    question: Which scheduled tests of every type run on my endpoint agents?
  phrasing_ops: 1
  slug: thousandeyes-endpoint-scheduled-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Enterprise Agent Cluster API from ThousandEyes — 2 operation(s) for enterprise agent cluster.
  name: ThousandEyes Enterprise Agent Cluster API
  phrasing_intents:
  - id: assignAgentToCluster
    intent: Add agents to an Enterprise Agent cluster
    question: How do I cluster several Enterprise Agents together?
  - id: unassignAgentFromCluster
    intent: Remove agents from an Enterprise Agent cluster
    question: Can I turn a cluster back into standalone Enterprise Agents?
  phrasing_ops: 2
  slug: thousandeyes-enterprise-agent-cluster-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Events API from ThousandEyes — 2 operation(s) for events.
  name: ThousandEyes Events API
  phrasing_intents:
  - id: getEvents
    intent: List events
    question: Which network events were detected in the last day?
  - id: getEvent
    intent: Get an event's details
    question: What was affected by a specific event?
  phrasing_ops: 2
  slug: thousandeyes-events-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The FTP Server Instant Tests API from ThousandEyes — 1 operation(s) for ftp server instant tests.
  name: ThousandEyes FTP Server Instant Tests API
  phrasing_intents:
  - id: createFtpServerInstantTest
    intent: Run an FTP server instant test
    question: Can I test an FTP download or upload once, right now?
  phrasing_ops: 1
  slug: thousandeyes-ftp-server-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: FTP Server test management operations
  name: ThousandEyes FTP Server Tests API
  phrasing_intents:
  - id: getFtpServerTests
    intent: List FTP Server tests
    question: Which FTP Server tests are watching our file servers?
  - id: createFtpServerTest
    intent: Create a scheduled FTP Server test
    question: Can I monitor an FTP server's availability on a schedule?
  - id: getFtpServerTest
    intent: Get an FTP Server test
    question: What agents and alert rules are on a given FTP Server test?
  - id: updateFtpServerTest
    intent: Update an FTP Server test
    question: Can I change the monitors on an FTP Server test?
  - id: deleteFtpServerTest
    intent: Delete an FTP Server test
    question: Can I remove an FTP Server test?
  phrasing_ops: 5
  slug: thousandeyes-ftp-server-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: A generic connector represents an instance of a third-party service that you can integrate with the ThousandEyes platform.
  name: ThousandEyes Generic Connectors API
  phrasing_intents:
  - id: getGenericConnector
    intent: Get a generic connector
    question: How do I see the target URL and headers of a connector?
  - id: updateGenericConnector
    intent: Update a generic connector
    question: How do I change where a generic connector sends data?
  - id: deleteGenericConnector
    intent: Delete a generic connector
    question: Is it possible to remove a generic connector?
  - id: listGenericConnectorOperations
    intent: List operations assigned to a connector
    question: Which operations are wired to a particular connector?
  - id: setGenericConnectorOperations
    intent: Assign operations to a connector
    question: Which call attaches operations to a generic connector?
  - id: getGenericConnectors
    intent: List generic connectors
    question: What generic connectors exist in my account group?
  - id: createGenericConnector
    intent: Create a generic connector
    question: How do I create a connector that sends data to my own endpoint?
  phrasing_ops: 7
  slug: thousandeyes-generic-connectors-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The HTTP Page Load Instant Tests API from ThousandEyes — 1 operation(s) for http page load instant tests.
  name: ThousandEyes HTTP Page Load Instant Tests API
  phrasing_intents:
  - id: createPageLoadInstantTest
    intent: Run an instant page load test
    question: Can I load a web page from several agents right now as a one-off?
  phrasing_ops: 1
  slug: thousandeyes-http-page-load-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The HTTP Server Endpoint Instant Scheduled Tests API from ThousandEyes — 1 operation(s) for http server endpoint instant scheduled tests.
  name: ThousandEyes HTTP Server Endpoint Instant Scheduled Tests API
  phrasing_intents:
  - id: createHttpServerScheduledInstantTest
    intent: Run an endpoint HTTP server instant test
    question: Can I have endpoint agents test a URL once, right away?
  phrasing_ops: 1
  slug: thousandeyes-http-server-endpoint-instant-scheduled-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The HTTP Server Endpoint Scheduled Test Results API from ThousandEyes — 3 operation(s) for http server endpoint scheduled test results.
  name: ThousandEyes HTTP Server Endpoint Scheduled Test Results API
  phrasing_intents:
  - id: getHttpServerScheduledTestResults
    intent: Get endpoint HTTP server test results
    question: What DNS, connect, wait and receive times did one endpoint HTTP test record?
  - id: getSingleTestFilteredHttpServerScheduledTestResults
    intent: Filter HTTP results for one endpoint test
    question: How do I filter one endpoint HTTP test's results by threshold?
  - id: getMultiTestFilteredHttpServerScheduledTestResults
    intent: Filter HTTP results across endpoint tests
    question: Is there a way to search HTTP results across all my endpoint scheduled tests at once?
  phrasing_ops: 3
  slug: thousandeyes-http-server-endpoint-scheduled-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The HTTP Server Endpoint Scheduled Tests API from ThousandEyes — 2 operation(s) for http server endpoint scheduled tests.
  name: ThousandEyes HTTP Server Endpoint Scheduled Tests API
  phrasing_intents:
  - id: getHttpServerEndpointScheduledTests
    intent: List HTTP server endpoint tests
    question: Which HTTP server tests are scheduled on my endpoint agents?
  - id: createHttpServerEndpointScheduledTest
    intent: Create an HTTP server endpoint test
    question: How do I monitor a web app's HTTP response from employee devices?
  - id: getHttpServerEndpointScheduledTest
    intent: Get an HTTP server endpoint test
    question: What URL and interval does a given endpoint HTTP server test use?
  - id: updateHttpServerEndpointScheduledTest
    intent: Update an HTTP server endpoint test
    question: Can I pause an endpoint HTTP server test without deleting it?
  - id: deleteHttpServerEndpointScheduledTest
    intent: Delete an HTTP server endpoint test
    question: Is there a way to delete an endpoint HTTP server test?
  phrasing_ops: 5
  slug: thousandeyes-http-server-endpoint-scheduled-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The HTTP Server Instant Tests API from ThousandEyes — 1 operation(s) for http server instant tests.
  name: ThousandEyes HTTP Server Instant Tests API
  phrasing_intents:
  - id: createHttpServerInstantTest
    intent: Run an instant HTTP server test
    question: Can I check a web server's HTTP availability right now without scheduling a test?
  phrasing_ops: 1
  slug: thousandeyes-http-server-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: HTTP Server test management operations
  name: ThousandEyes HTTP Server Tests API
  phrasing_intents:
  - id: getHttpServerTests
    intent: List HTTP Server tests
    question: Which HTTP Server tests are monitoring our websites?
  - id: createHttpServerTest
    intent: Create a scheduled HTTP Server test
    question: Can I monitor a URL's availability and response time on a schedule?
  - id: getHttpServerTest
    intent: Get an HTTP Server test
    question: What agents and alert rules does one HTTP Server test use?
  - id: updateHttpServerTest
    intent: Update an HTTP Server test
    question: Can I change the monitors on an HTTP Server test?
  - id: deleteHttpServerTest
    intent: Delete an HTTP Server test
    question: Can I remove an HTTP Server test?
  phrasing_ops: 5
  slug: thousandeyes-http-server-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Instant Tests API from ThousandEyes — 1 operation(s) for instant tests.
  name: ThousandEyes Instant Tests API
  phrasing_intents:
  - id: runInstantTest
    intent: Rerun an existing instant test
    question: Can I rerun an instant test I already created?
  phrasing_ops: 1
  slug: thousandeyes-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Internet Insights Catalog Providers API from ThousandEyes — 2 operation(s) for internet insights catalog providers.
  name: ThousandEyes Internet Insights Catalog Providers API
  phrasing_intents:
  - id: filterCatalogProviders
    intent: Search Internet Insights catalog providers
    question: Which network and application providers are in the Internet Insights catalog?
  - id: getCatalogProvider
    intent: Get a catalog provider
    question: How do I get the full details of one Internet Insights provider?
  phrasing_ops: 2
  slug: thousandeyes-internet-insights-catalog-providers-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Internet Insights Outages API from ThousandEyes — 3 operation(s) for internet insights outages.
  name: ThousandEyes Internet Insights Outages API
  phrasing_intents:
  - id: filterOutages
    intent: Search network and application outages
    question: Were there internet outages affecting a given provider recently?
  - id: getNetworkOutage
    intent: Get a network outage
    question: What locations and interfaces were hit by a specific network outage?
  - id: getAppOutage
    intent: Get an application outage
    question: What servers were affected by a specific application outage?
  phrasing_ops: 3
  slug: thousandeyes-internet-insights-outages-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Local Network Endpoint Test Results API from ThousandEyes — 3 operation(s) for local network endpoint test results.
  name: ThousandEyes Local Network Endpoint Test Results API
  phrasing_intents:
  - id: getLocalNetworksTestResults
    intent: List local networks used by endpoint agents
    question: Which local networks are my endpoint agents connected through?
  - id: filterLocalNetworksTestResultsTopologies
    intent: Search local network topology probes
    question: How do I find local network topology probes for a date range?
  - id: getLocalNetworksTestResultsTopology
    intent: Get a local network topology
    question: What does the local network path look like for one topology?
  phrasing_ops: 3
  slug: thousandeyes-local-network-endpoint-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Local Problems API from ThousandEyes — 1 operation(s) for local problems.
  name: ThousandEyes Local Problems API
  phrasing_intents:
  - id: getAgentsLocalProblems
    intent: List Cloud Agents with local problems
    question: Which Cloud Agents had local impairments that could skew my results?
  phrasing_ops: 1
  slug: thousandeyes-local-problems-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Network BGP Test Results API from ThousandEyes — 2 operation(s) for network bgp test results.
  name: ThousandEyes Network BGP Test Results API
  phrasing_intents:
  - id: getTestBgpResults
    intent: Get BGP test results
    question: Which BGP monitors can see our target prefix, and how reachable is it?
  - id: getTestBgpRoutesPrefixRoundResults
    intent: Get BGP routes for a prefix in a round
    question: What AS path did a prefix take in a given BGP test round?
  phrasing_ops: 2
  slug: thousandeyes-network-bgp-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Network Dynamic Endpoint Test Results API from ThousandEyes — 3 operation(s) for network dynamic endpoint test results.
  name: ThousandEyes Network Dynamic Endpoint Test Results API
  phrasing_intents:
  - id: filterDynamicTestNetworkResults
    intent: Get network results for a dynamic test
    question: What loss, latency, jitter and bandwidth did endpoint agents see on a dynamic test?
  - id: getDynamicTestPathVisResults
    intent: Get path visualization for a dynamic test
    question: What route did endpoint agents take to the destination of a dynamic test?
  - id: getDynamicTestPathVisAgentRoundResults
    intent: Get hop-by-hop path for a dynamic test round
    question: Can I see each hop one endpoint agent crossed in a round of a dynamic test?
  phrasing_ops: 3
  slug: thousandeyes-network-dynamic-endpoint-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Network Endpoint Scheduled Test Results API from ThousandEyes — 4 operation(s) for network endpoint scheduled test results.
  name: ThousandEyes Network Endpoint Scheduled Test Results API
  phrasing_intents:
  - id: filterScheduledTestNetworkResults
    intent: Get network results for one scheduled test
    question: What loss, latency and jitter did endpoint agents see for a scheduled test?
  - id: filterScheduledTestsNetworkResults
    intent: Get network results across scheduled tests
    question: Can I pull endpoint network metrics for several scheduled tests at once?
  - id: getScheduledTestPathVisResults
    intent: Get path visualization for a scheduled test
    question: What network path did endpoint agents take for a scheduled test?
  - id: getScheduledTestPathVisAgentRoundResults
    intent: Get hop-by-hop path for a scheduled test round
    question: Can I see every hop for one endpoint agent in one round of a scheduled test?
  phrasing_ops: 4
  slug: thousandeyes-network-endpoint-scheduled-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Network Test Results API from ThousandEyes — 3 operation(s) for network test results.
  name: ThousandEyes Network Test Results API
  phrasing_intents:
  - id: getTestNetworkResults
    intent: Get network test results
    question: What latency, loss and jitter did my test record in the latest round?
  - id: getTestPathVisResults
    intent: Get path visualization results
    question: How do I see the hop-by-hop path my test traffic took?
  - id: getTestPathVisAgentRoundResults
    intent: Get path trace for one agent round
    question: Which route did a single agent take in one round of my test?
  phrasing_ops: 3
  slug: thousandeyes-network-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Manage the connectors assigned to an operation.
  name: ThousandEyes Operation Connectors API
  phrasing_intents:
  - id: getOperationConnectors
    intent: List connectors assigned to an operation
    question: Which connectors is a given operation sending through?
  - id: setOperationConnectors
    intent: Assign connectors to an operation
    question: How do I attach connectors to an operation?
  phrasing_ops: 2
  slug: thousandeyes-operation-connectors-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Page Load test management operations
  name: ThousandEyes Page Load Tests API
  phrasing_intents:
  - id: getPageLoadTests
    intent: List Page Load tests
    question: What Page Load tests are configured in my account?
  - id: createPageLoadTest
    intent: Create a Page Load test
    question: How do I measure full browser page load time on a schedule?
  - id: getPageLoadTest
    intent: Get a Page Load test
    question: Which agents and alert rules does a Page Load test use?
  - id: updatePageLoadTest
    intent: Update a Page Load test
    question: What fields are editable on a shared Page Load test?
  - id: deletePageLoadTest
    intent: Delete a Page Load test
    question: Can I delete a Page Load test?
  phrasing_ops: 5
  slug: thousandeyes-page-load-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: A Panorama connector represents an instance of Palo Alto Networks Panorama that you can integrate with the ThousandEyes platform.
  name: ThousandEyes Panorama Connectors API
  phrasing_intents:
  - id: getPanoramaConnector
    intent: Get a Panorama connector
    question: What's configured on a specific Panorama connector?
  - id: updatePanoramaConnector
    intent: Replace a Panorama connector's configuration
    question: Do I have to resend credentials when updating a Panorama connector?
  - id: deletePanoramaConnector
    intent: Delete a Panorama connector
    question: Can I remove a Panorama connector entirely?
  - id: getPanoramaConnectorOperations
    intent: List operations assigned to a Panorama connector
    question: Which operations are tied to my Panorama connector?
  - id: setPanoramaConnectorOperations
    intent: Assign operations to a Panorama connector
    question: Can I clear all operation assignments from a Panorama connector?
  - id: getPanoramaConnectors
    intent: List Panorama connectors
    question: Which Panorama connectors do we have configured?
  - id: createPanoramaConnector
    intent: Create a Panorama connector
    question: Can ThousandEyes connect to Palo Alto Panorama?
  phrasing_ops: 7
  slug: thousandeyes-panorama-connectors-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Path Visualization Interface Groups API from ThousandEyes — 2 operation(s) for path visualization interface groups.
  name: ThousandEyes Path Visualization Interface Groups API
  phrasing_intents:
  - id: getPathVisInterfaceGroups
    intent: List path visualization interface groups
    question: What interface groups are defined for path visualization?
  - id: createPathVisInterfaceGroups
    intent: Create a path visualization interface group
    question: How do I group router interfaces by IP address in path visualization?
  - id: updatePathVisInterfaceGroup
    intent: Update a path visualization interface group
    question: Can I add IP addresses to an existing interface group?
  - id: deletePathVisInterfaceGroup
    intent: Delete a path visualization interface group
    question: How do I delete an interface group from path visualization?
  phrasing_ops: 4
  slug: thousandeyes-path-visualization-interface-groups-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Permission GET operation
  name: ThousandEyes Permissions API
  phrasing_intents:
  - id: getPermissions
    intent: List assignable permissions
    question: Which permissions can be assigned to a role?
  phrasing_ops: 1
  slug: thousandeyes-permissions-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Quota CRUD Operation
  name: ThousandEyes Quotas API
  phrasing_intents:
  - id: getQuotas
    intent: View organization and account group quotas
    question: How much usage quota is allotted to each organization and account group?
  - id: assignOrganizationsQuotas
    intent: Set organization quotas
    question: Can I set or change the usage quota for an organization?
  - id: unassignOrganizationsQuotas
    intent: Remove organization quotas
    question: Can I take the quota off an organization entirely?
  - id: assignOrganizationsAccountGroupsQuotas
    intent: Set account group quotas
    question: Can I give individual account groups their own quota across organizations?
  - id: unassignOrganizationsAccountGroupsQuotas
    intent: Remove account group quotas
    question: Can I remove quotas from specific account groups?
  phrasing_ops: 5
  slug: thousandeyes-quotas-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Real User Endpoint Test Results API from ThousandEyes — 5 operation(s) for real user endpoint test results.
  name: ThousandEyes Real User Endpoint Test Results API
  phrasing_intents:
  - id: filterRealUserTestsResults
    intent: Search endpoint real user test results
    question: How do I see what real users experienced over the last day?
  - id: getRealUserTestResults
    intent: Get one endpoint real user test
    question: What detail is recorded for a single real user test?
  - id: filterRealUserTestsVisitedPagesResults
    intent: Search pages visited in real user tests
    question: Which web pages did my users visit during real user tests?
  - id: getRealUserTestPageResults
    intent: Get a real user page's waterfall
    question: How do I see the full request waterfall for one page a user loaded?
  - id: filterRealUserTestsNetworkResults
    intent: Search networks seen in real user tests
    question: What networks were my users on during real user tests?
  phrasing_ops: 5
  slug: thousandeyes-real-user-endpoint-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Role CRUD operations
  name: ThousandEyes Roles API
  phrasing_intents:
  - id: getRoles
    intent: List roles
    question: Which user roles are defined in my account?
  - id: createRole
    intent: Create a custom role
    question: Can I define a custom role with only certain permissions?
  - id: getRole
    intent: Get a role's permissions
    question: What permissions does a specific role grant?
  - id: updateRole
    intent: Update a user-defined role
    question: Do I need to send the full permission list when editing a role?
  - id: deleteRole
    intent: Delete a role
    question: Can I delete a custom role we no longer use?
  phrasing_ops: 5
  slug: thousandeyes-roles-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Run Endpoint Instant Scheduled Tests API from ThousandEyes — 1 operation(s) for run endpoint instant scheduled tests.
  name: ThousandEyes Run Endpoint Instant Scheduled Tests API
  phrasing_intents:
  - id: runEndpointScheduledInstantTest
    intent: Run an existing endpoint scheduled test now
    question: Can I trigger an existing endpoint scheduled test immediately?
  phrasing_ops: 1
  slug: thousandeyes-run-endpoint-instant-scheduled-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The SIP Server Instant Tests API from ThousandEyes — 1 operation(s) for sip server instant tests.
  name: ThousandEyes SIP Server Instant Tests API
  phrasing_intents:
  - id: createSipServerInstantTest
    intent: Run a SIP server instant test
    question: Can I check a SIP server's availability on demand?
  phrasing_ops: 1
  slug: thousandeyes-sip-server-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: SIP Server test management operations
  name: ThousandEyes SIP Server Tests API
  phrasing_intents:
  - id: getSipServerTests
    intent: List SIP Server tests
    question: Which SIP Server tests are configured?
  - id: createSipServerTest
    intent: Create a SIP Server test
    question: How do I monitor whether my SIP server accepts registrations?
  - id: getSipServerTest
    intent: Get a SIP Server test
    question: What agents and alert rules are on a SIP Server test?
  - id: updateSipServerTest
    intent: Update a SIP Server test
    question: Can I change the interval of an existing SIP Server test?
  - id: deleteSipServerTest
    intent: Delete a SIP Server test
    question: How do I delete a SIP Server test?
  phrasing_ops: 5
  slug: thousandeyes-sip-server-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Configure data streaming
  name: ThousandEyes Streaming API
  phrasing_intents:
  - id: getStreams
    intent: List data streams
    question: Which data streams are exporting our test data?
  - id: createStream
    intent: Create a data stream
    question: Can I stream test metrics to an OpenTelemetry collector?
  - id: getStream
    intent: Get a data stream
    question: What endpoint and filters does a specific data stream use?
  - id: updateStream
    intent: Update a data stream
    question: Are fields replaced or appended when I update a data stream?
  - id: deleteStream
    intent: Delete a data stream
    question: Can I stop and remove a data stream?
  phrasing_ops: 5
  slug: thousandeyes-streaming-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Assign tags to other objects
  name: ThousandEyes Tag Assignment API
  phrasing_intents:
  - id: assignTags
    intent: Assign several tags to objects
    question: Can I attach several tags to many tests in one call?
  - id: unassignTags
    intent: Remove several tags from objects
    question: Can I strip multiple tags from many objects at once?
  - id: assignTag
    intent: Assign one tag to objects
    question: Can I apply a single tag to a list of tests or agents?
  - id: unassignTag
    intent: Remove one tag from objects
    question: Can I take a single tag off several objects?
  phrasing_ops: 4
  slug: thousandeyes-tag-assignment-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Tag CRUD Operations
  name: ThousandEyes Tags API
  phrasing_intents:
  - id: getTags
    intent: List tags
    question: What tags exist in my account group?
  - id: createTag
    intent: Create a single tag
    question: Can I create a key/value tag with its own color and icon?
  - id: createTags
    intent: Create many tags in one request
    question: Can I create a batch of tags at once and see which ones failed?
  - id: getTag
    intent: Get a tag
    question: Can I look up a single tag by its ID?
  - id: updateTag
    intent: Update a tag
    question: Can I change a tag's value or color after it's created?
  - id: deleteTag
    intent: Delete a tag
    question: Can I permanently delete a tag I no longer use?
  phrasing_ops: 6
  slug: thousandeyes-tags-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Templates API from ThousandEyes — 4 operation(s) for templates.
  name: ThousandEyes Templates API
  phrasing_intents:
  - id: createTemplate
    intent: Create a template
    question: Can I package tests, alert rules and dashboards into a reusable template?
  - id: getTemplates
    intent: List templates
    question: What templates do I have available in ThousandEyes?
  - id: getTemplate
    intent: Get a template
    question: What is defined inside one particular template?
  - id: updateTemplate
    intent: Replace a template's definition
    question: Does updating a template overwrite the whole object?
  - id: deleteTemplate
    intent: Delete a template
    question: How do I remove a template I no longer use?
  - id: deployTemplate
    intent: Deploy a template
    question: What happens when I deploy a template?
  - id: getSharingSettings
    intent: Get a template's sharing settings
    question: Who can see a template I built?
  - id: updateSharingSettings
    intent: Change a template's sharing scope
    question: Can I share a template with the rest of my organization?
  phrasing_ops: 8
  slug: thousandeyes-templates-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Test Snapshots API from ThousandEyes — 1 operation(s) for test snapshots.
  name: ThousandEyes Test Snapshots API
  phrasing_intents:
  - id: createTestSnapshot
    intent: Share a snapshot of test data
    question: Can I share a test's results for a time range with someone outside my account?
  phrasing_ops: 1
  slug: thousandeyes-test-snapshots-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Get all tests
  name: ThousandEyes Tests API
  phrasing_intents:
  - id: getTests
    intent: List all configured tests
    question: What tests of every type do we have configured?
  - id: getTestVersionHistory
    intent: Get a test's version history
    question: Who changed a test and when?
  phrasing_ops: 2
  slug: thousandeyes-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Tests Assignment on Agents API from ThousandEyes — 3 operation(s) for tests assignment on agents.
  name: ThousandEyes Tests Assignment on Agents API
  phrasing_intents:
  - id: assignTests
    intent: Add tests to an agent
    question: Can I add tests to an agent without removing the ones it already runs?
  - id: overwriteTests
    intent: Replace all tests on an agent
    question: Can I replace every test on an agent with a new set?
  - id: unassignTests
    intent: Remove tests from an agent
    question: Can I stop an agent from running specific tests?
  phrasing_ops: 3
  slug: thousandeyes-tests-assignment-on-agents-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Usage GET Operation
  name: ThousandEyes Usage API
  phrasing_intents:
  - id: getUsage
    intent: Get usage for the current period
    question: How many units has my organization used this billing period?
  - id: getEnterpriseAgentsUnitsUsage
    intent: Get enterprise agent unit usage
    question: How many units are my enterprise agents consuming?
  - id: getTestsUnitsUsage
    intent: Get unit usage by test
    question: Which tests are consuming the most cloud and enterprise agent units?
  phrasing_ops: 3
  slug: thousandeyes-usage-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: User events GET operation
  name: ThousandEyes User Events API
  phrasing_intents:
  - id: getUserEvents
    intent: List activity log events
    question: Who made changes in our account recently?
  phrasing_ops: 1
  slug: thousandeyes-user-events-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: User CRUD operations
  name: ThousandEyes Users API
  phrasing_intents:
  - id: getUsers
    intent: List users
    question: Who are all the users in my ThousandEyes organization?
  - id: createUser
    intent: Invite a new user
    question: How do I add a new user and give them roles in specific account groups?
  - id: getUser
    intent: Get a user
    question: Where can I see a particular user's roles and account groups?
  - id: updateUser
    intent: Update a user
    question: How do I change a user's email address or roles?
  - id: deleteUser
    intent: Delete a user
    question: Someone left the team; can I remove their user account?
  - id: getCurrentUser
    intent: Get the current user
    question: Who am I logged in as through the API?
  phrasing_ops: 6
  slug: thousandeyes-users-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Voice Instant Tests API from ThousandEyes — 1 operation(s) for voice instant tests.
  name: ThousandEyes Voice Instant Tests API
  phrasing_intents:
  - id: createVoiceInstantTest
    intent: Run an instant voice test
    question: Can I measure call quality between two agents right now?
  phrasing_ops: 1
  slug: thousandeyes-voice-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Voice RTP Server Test Results API from ThousandEyes — 1 operation(s) for voice rtp server test results.
  name: ThousandEyes Voice RTP Server Test Results API
  phrasing_intents:
  - id: getTestRtpServerResults
    intent: Get RTP server voice test metrics
    question: What MOS, loss and jitter did a voice RTP test record?
  phrasing_ops: 1
  slug: thousandeyes-voice-rtp-server-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Voice SIP Server Test Results API from ThousandEyes — 1 operation(s) for voice sip server test results.
  name: ThousandEyes Voice SIP Server Test Results API
  phrasing_intents:
  - id: getTestSipServerResults
    intent: Get SIP server test results
    question: Did my SIP server respond and register successfully in the last round?
  phrasing_ops: 1
  slug: thousandeyes-voice-sip-server-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Voice test management operations
  name: ThousandEyes Voice Tests API
  phrasing_intents:
  - id: getVoiceTests
    intent: List Voice tests
    question: What Voice tests do I have?
  - id: createVoiceTest
    intent: Create a Voice test
    question: How do I measure call quality between two agents on a schedule?
  - id: getVoiceTest
    intent: Get a Voice test
    question: Which agents and interval does a Voice test use?
  - id: updateVoiceTest
    intent: Update a Voice test
    question: What can I change on a shared Voice test?
  - id: deleteVoiceTest
    intent: Delete a Voice test
    question: How do I delete a Voice test?
  phrasing_ops: 5
  slug: thousandeyes-voice-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Web FTP Server Test Results API from ThousandEyes — 1 operation(s) for web ftp server test results.
  name: ThousandEyes Web FTP Server Test Results API
  phrasing_intents:
  - id: getTestFtpServerResults
    intent: Get FTP server test results
    question: How did an FTP server test perform in its latest round?
  phrasing_ops: 1
  slug: thousandeyes-web-ftp-server-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Web HTTP Server Test Results API from ThousandEyes — 1 operation(s) for web http server test results.
  name: ThousandEyes Web HTTP Server Test Results API
  phrasing_intents:
  - id: getTestHttpServerResults
    intent: Get HTTP server test results
    question: What were the DNS, connect, wait and receive times for my HTTP server test?
  phrasing_ops: 1
  slug: thousandeyes-web-http-server-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Web Page Load Test Results API from ThousandEyes — 2 operation(s) for web page load test results.
  name: ThousandEyes Web Page Load Test Results API
  phrasing_intents:
  - id: getTestPageLoadResults
    intent: Get page load test results
    question: What page load and DOM load times did my test measure?
  - id: getTestPageLoadAgentRoundResults
    intent: Get page load HAR for an agent round
    question: How do I download the HAR waterfall for one agent's page load?
  phrasing_ops: 2
  slug: thousandeyes-web-page-load-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Web Transaction Instant Tests API from ThousandEyes — 1 operation(s) for web transaction instant tests.
  name: ThousandEyes Web Transaction Instant Tests API
  phrasing_intents:
  - id: createWebTransactionInstantTest
    intent: Run a web transactions instant test
    question: Can I run a scripted web transaction once, on demand?
  phrasing_ops: 1
  slug: thousandeyes-web-transaction-instant-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Web Transactions test management operations
  name: ThousandEyes Web Transaction Tests API
  phrasing_intents:
  - id: getWebTransactionsTests
    intent: List Web Transactions tests
    question: Which scripted Web Transactions tests are configured?
  - id: createWebTransactionsTest
    intent: Create a scheduled Web Transactions test
    question: Can I script a multi-step user journey and run it on a schedule?
  - id: getWebTransactionsTest
    intent: Get a Web Transactions test
    question: What agents and alert rules are on a Web Transactions test?
  - id: updateWebTransactionsTest
    intent: Update a Web Transactions test
    question: Can I swap the credentials a Web Transactions test uses?
  - id: deleteWebTransactionsTest
    intent: Delete a Web Transactions test
    question: Can I remove a Web Transactions test?
  phrasing_ops: 5
  slug: thousandeyes-web-transaction-tests-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: The Web Transactions Test Results API from ThousandEyes — 4 operation(s) for web transactions test results.
  name: ThousandEyes Web Transactions Test Results API
  phrasing_intents:
  - id: getTestWebTransactionResults
    intent: Get web transaction test results
    question: How did my scripted web transaction perform in the latest round?
  - id: getTestWebTransactionAgentRoundResults
    intent: Get web transaction results for an agent round
    question: Which call shows what one agent saw in one transaction round?
  - id: getTestWebTransactionAgentRoundPageResults
    intent: Get one page of a web transaction run
    question: How do I see timings for one page inside a web transaction?
  - id: getTestConsoleLogsAgentRoundResults
    intent: Get browser console logs from a transaction run
    question: Can I see browser console errors from a web transaction test?
  phrasing_ops: 4
  slug: thousandeyes-web-transactions-test-results-api
- baseURL: https://api.thousandeyes.com/v7
  baseurl_source: declared
  description: Webhook operations allow you to customize the payload of generic connectors.
  name: ThousandEyes Webhook Operations API
  phrasing_intents:
  - id: getWebhookOperation
    intent: Get a webhook operation
    question: What payload and headers does a webhook operation send?
  - id: updateWebhookOperation
    intent: Update a webhook operation
    question: How do I change the payload template of a webhook operation?
  - id: deleteWebhookOperation
    intent: Delete a webhook operation
    question: Is there a way to delete a webhook operation?
  - id: getWebhookOperations
    intent: List webhook operations
    question: What webhook operations are configured in my account group?
  - id: createWebhookOperation
    intent: Create a webhook operation
    question: How do I send alert notifications to my own webhook?
  phrasing_ops: 5
  slug: thousandeyes-webhook-operations-api
artifact_total: 107
asyncapis:
- description: ''
  name: Thousandeyes Webhooks
  slug: thousandeyes-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/capabilities/thousandeyes-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thousandeyes-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-administrative-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-administrative-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-api-token-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-api-token-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-agents-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-alerts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-alerts-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-autonomous-systems-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-autonomous-systems-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-bgp-monitors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-bgp-monitors-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-cloud-insights-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-cloud-insights-integrations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-credentials-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-credentials-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-dashboards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-dashboards-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-emulation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-emulation-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-endpoint-agents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-endpoint-agents-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-endpoint-instant-scheduled-tests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-endpoint-instant-scheduled-tests-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-endpoint-agent-labels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-endpoint-agent-labels-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-endpoint-test-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-endpoint-test-results-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-endpoint-tests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-endpoint-tests-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-event-detection-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-event-detection-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-integrations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-internet-insights-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-internet-insights-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-test-snapshots-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-test-snapshots-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-tags-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-templates-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-tests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-tests-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-instant-tests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-instant-tests-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-test-results-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-test-results-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-opentelemetry-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-opentelemetry-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/overlays/thousandeyes-usage-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thousandeyes-usage-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/security/thousandeyes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thousandeyes-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/authentication/thousandeyes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thousandeyes-authentication.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/thousandeyes/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thousandeyes.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cisco.com/docs/thousandeyes/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thousandeyes
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/CiscoDevNet/ThousandEyes-MCP-Server-official
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/thousandeyes/thousandeyes-sdk-python
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: company
  title: ''
  type: Website
  url: https://www.thousandeyes.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/thousandeyes/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.cisco.com/docs/thousandeyes/getting-started/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.thousandeyes.com/product-documentation/getting-started/getting-started-with-the-thousandeyes-api
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/docs/thousandeyes/developer-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.thousandeyes.com/
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/t5/thousandeyes/bd-p/disc-thousandeyes
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/cisco-thousandeyes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thousandeyes.com
- group: start
  title: ''
  type: Login
  url: https://app.thousandeyes.com/login
- group: start
  title: ''
  type: SignUp
  url: https://app.thousandeyes.com/login?fwd=%2Fsignup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cisco.com/c/en/us/products/collateral/security/cisco-thousandeyes-og.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.cisco.com/site/license/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/cisco/cisco-devnet-s-public-workspace/collection/v2ogbsf/cisco-thousandeyes-api-v7
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.cisco.com/docs/thousandeyes/thousandeyes-api-license-terms-and-support-policy/
- group: auth
  title: ''
  type: Security
  url: https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://trustportal.cisco.com/c/r/ctp/trust-portal.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/packages/thousandeyes-packages.yml
  title: ''
  type: SDKs
  url: packages/thousandeyes-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/packages/thousandeyes-packages.yml
  title: ''
  type: Packages
  url: packages/thousandeyes-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/cli/thousandeyes-cli.yml
  title: ''
  type: CLI
  url: cli/thousandeyes-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/well-known/thousandeyes-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thousandeyes-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/llms/thousandeyes-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thousandeyes-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/mcp/thousandeyes-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thousandeyes-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/mcp/thousandeyes-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/thousandeyes-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/conformance/thousandeyes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thousandeyes-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/errors/thousandeyes-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thousandeyes-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/lifecycle/thousandeyes-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thousandeyes-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/scopes/thousandeyes-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/thousandeyes-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/security/thousandeyes-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thousandeyes-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/security/thousandeyes-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thousandeyes-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/conventions/thousandeyes-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thousandeyes-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/changelog/thousandeyes-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thousandeyes-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/data-model/thousandeyes-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thousandeyes-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/plans/thousandeyes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thousandeyes-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/rate-limits/thousandeyes-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thousandeyes-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/asyncapi/thousandeyes-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thousandeyes-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-19'
description: ThousandEyes is Cisco's digital experience monitoring platform, acquired in 2020 and operated as part of Cisco Networking. It runs a global fleet of Cloud, Enterprise, Endpoint and Connected Device agents that measure network paths, BGP routing, DNS, application response and internet outages end to end, then exposes that telemetry through the ThousandEyes v7 REST API. The v7 API is documented on Cisco DevNet and publishes 26 downloadable OpenAPI 3.0 documents plus a unified document covering 326 operations across tests, instant tests, test results, agents, endpoint agents, alerts, event detection, dashboards, tags, templates, integrations, credentials, Internet Insights, Cloud Insights, usage and administration. Authentication is a bearer API token, with an OAuth 2.0 authorization-code and device-code flow advertised anonymously at /.well-known/oauth-authorization-server. Cisco also runs a remote MCP server at https://api.thousandeyes.com/mcp with about 51 documented tools,
  generated SDKs for Python, Java and Go, a Go CLI, a Terraform provider, a public Postman collection and a ThousandEyes for Government FedRAMP Moderate instance.
image: https://docs.thousandeyes.com/~gitbook/image?url=https%3A%2F%2F1112912342-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fspaces%252F-M4QARF6s57qxMrOHDTZ%252Favatar-1586888079651.png%3Fgeneration%3D1586888079959831%26alt%3Dmedia&width=180&height=180&sign=8b5c0248&sv=2
layout: provider
mcp_servers:
- description: Remote MCP server at api.thousandeyes.com over HTTP requiring OAuth; 51 tools listed.
  name: ThousandEyes MCP Server
  slug: thousandeyes-mcp-server
modified: '2026-08-19'
name: ThousandEyes
nav: Providers
network: true
overview: 'ThousandEyes publishes 98 APIs on the [APIs.io](https://apis.io/) network, including Account Groups API, Agent Proxies API, Agent to Agent Instant Tests API, and 95 more. Tagged areas include Monitoring, Network Visibility, Digital Experience, Observability, and Networking.


  The ThousandEyes catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThousandEyes'' developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, quickstart, support, and 68 more developer resources.'
plans:
- name: Thousandeyes Plans Pricing
  plan_count: 7
  slug: thousandeyes-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Thousandeyes Rate Limits
  slug: thousandeyes-rate-limits
scopes:
- name: Thousandeyes Scopes
  scope_count: 2
  slug: thousandeyes-scopes
  summary_line: 2 scopes · authorizationCode/deviceCode
score:
  band: exemplar
  composite: 75.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 63.0
    developer_ergonomics: 75.6
    discoverability: 80.0
    operational_transparency: 92.1
  previous_composite: 75.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 98
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/thousandeyes/refs/heads/main/screenshots/thousandeyes-2026-09-02T163600.png
security:
- kind: authentication
  name: Thousandeyes Authentication
  slug: thousandeyes-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Thousandeyes Domain Security
  slug: thousandeyes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thousandeyes Vulnerability Disclosure
  slug: thousandeyes-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Thousandeyes Trust Center
  slug: thousandeyes-trust-center
  summary_line: FedRAMP Moderate
slug: thousandeyes
tags:
- Monitoring
- Network Visibility
- Digital Experience
- Observability
- Networking
- Enterprise
- Synthetic Monitoring
- BGP
- Internet Insights
- Endpoint Monitoring
- OpenTelemetry
- Cisco
website: https://www.thousandeyes.com/
---
