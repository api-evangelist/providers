---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 59.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 116
  human_in_the_loop: 0
  name: Checkly Agentic Access
  operation_count: 231
  slug: checkly-agentic-access
  summary_line: 231 operations · 116 acting
api_count: 1
apis:
- description: Checkly is a monitoring-as-code platform for API and synthetic monitoring with Playwright-based browser checks and programmable API checks.
  name: Checkly
  slug: checkly
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Accounts API from Checkly — 11 operation(s) for accounts.
  name: Checkly Accounts API
  phrasing_intents:
  - id: getV1Accounts
    intent: List accounts my API key can access
    question: Which Checkly accounts does my API key have access to?
  - id: getV1AccountsMe
    intent: Get the current account's details
    question: What are the details of the account I'm currently using?
  - id: getV1AccountsMeEntitlements
    intent: Get the current account's plan entitlements
    question: What features and limits does my current plan include?
  - id: getV1AccountsMeMembers
    intent: List members and invites of my account
    question: Who are the members of my current account, and who still has an invite pending?
  - id: deleteV1AccountsMeMembersUserid
    intent: Remove a member from my account
    question: How do I remove someone from the account I'm currently using?
  - id: patchV1AccountsMeMembersUserid
    intent: Change a member's role on my account
    question: Can I promote a member of my current account to a different role?
  - id: getV1AccountsAccountid
    intent: Get a specific account's details
    question: What are the details of a particular account by its ID?
  - id: getV1AccountsAccountidEntitlements
    intent: Get a specific account's plan entitlements
    question: Which features and limits does a given account's plan allow?
  phrasing_ops: 11
  slug: checkly-accounts-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Alert Channels API from Checkly — 6 operation(s) for alert channels.
  name: Checkly Alert Channels API
  phrasing_intents:
  - id: getV1Alertchannels
    intent: List alert channels
    question: Which alert channels are set up in my Checkly account?
  - id: postV1Alertchannels
    intent: Create an alert channel
    question: How do I get notified by email or chat when a check fails?
  - id: deleteV1AlertchannelsId
    intent: Delete an alert channel
    question: How do I remove an alert channel I no longer use?
  - id: getV1AlertchannelsId
    intent: Get an alert channel
    question: What config and subscriptions does a specific alert channel have?
  - id: putV1AlertchannelsId
    intent: Update an alert channel
    question: How do I change where an existing alert channel sends notifications?
  - id: putV1AlertchannelsIdSubscriptions
    intent: Subscribe a check or group to an alert channel
    question: How do I make one check send its failure alerts to a particular channel?
  phrasing_ops: 6
  slug: checkly-alert-channels-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Analytics API from Checkly — 12 operation(s) for analytics.
  name: Checkly Analytics API
  phrasing_intents:
  - id: getV1AnalyticsApichecksId
    intent: Get performance metrics for an API check
    question: What was the p99 DNS time and availability of my API check last week?
  - id: getV1AnalyticsBrowserchecksId
    intent: Get performance metrics for a browser check
    question: How many console errors did my browser check hit on average this month?
  - id: postV1AnalyticsChecks
    intent: Summarize analytics for several checks at once
    question: Can I get availability and response times for a batch of checks in one call?
  - id: getV1AnalyticsDnsId
    intent: Get performance metrics for a DNS monitor
    question: What's the p95 total DNS query time for my DNS monitor today?
  - id: getV1AnalyticsHeartbeatchecksId
    intent: Get availability metrics for a heartbeat check
    question: How often did my cron job's heartbeat ping arrive late or early?
  - id: getV1AnalyticsIcmpId
    intent: Get latency and packet loss for an ICMP monitor
    question: What packet loss percentage did my ICMP ping monitor see yesterday?
  - id: getV1AnalyticsMetrics
    intent: List reporting metrics available per check type
    question: Which metric names can I request from Checkly analytics for a given check type?
  - id: getV1AnalyticsMultistepchecksId
    intent: Get performance metrics for a multistep check
    question: How did my multistep check perform over the last 24 hours?
  phrasing_ops: 12
  slug: checkly-analytics-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Check Alerts API from Checkly — 2 operation(s) for check alerts.
  name: Checkly Check Alerts API
  phrasing_intents:
  - id: getV1Checkalerts
    intent: List alerts across all checks
    question: Which alerts fired across my whole account in the last six hours?
  - id: getV1CheckalertsCheckid
    intent: List alerts for one check
    question: What alerts has a specific check triggered recently?
  phrasing_ops: 2
  slug: checkly-check-alerts-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Check Groups API from Checkly — 11 operation(s) for check groups.
  name: Checkly Check Groups API
  phrasing_intents:
  - id: getV1Checkgroups
    intent: List check groups
    question: Which check groups exist in my Checkly account?
  - id: postV1Checkgroups
    intent: Create a check group (v1)
    question: How do I create a group to share settings across checks using the v1 endpoint?
  - id: getV1CheckgroupsGroupidChecksCheckid
    intent: Get a grouped check with group settings (v1)
    question: What does a check look like once its group's settings are applied, including project fields?
  - id: deleteV1CheckgroupsId
    intent: Delete a check group
    question: Can I delete a check group that still has checks in it?
  - id: getV1CheckgroupsId
    intent: Get a check group
    question: What settings and locations does a specific check group use?
  - id: putV1CheckgroupsId
    intent: Update a check group (v1)
    question: How do I mute every check in a group at once with the v1 endpoint?
  - id: getV1CheckgroupsIdChecks
    intent: List a group's checks with settings applied (v1)
    question: What are the effective settings of all checks in one group, v1 style with project fields?
  - id: postV2Checkgroups
    intent: Create a check group (v2)
    question: How do I create a check group through the newer v2 endpoint?
  phrasing_ops: 11
  slug: checkly-check-groups-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Check Results API from Checkly — 4 operation(s) for check results.
  name: Checkly Check Results API
  phrasing_intents:
  - id: getV1CheckresultsCheckid
    intent: List a check's raw results (deprecated v1)
    question: Can I still page through a check's raw results with the older page-numbered endpoint?
  - id: getV1CheckresultsCheckidCheckresultid
    intent: Get a single check result
    question: What happened in one specific run of a check?
  - id: getV1CheckresultsCheckidCheckresultidAssets
    intent: List downloadable assets of a check result
    question: Where can I download screenshots or traces from a check run?
  - id: getV2CheckresultsCheckid
    intent: List a check's raw results
    question: What were the recent results of one of my checks between two dates?
  phrasing_ops: 4
  slug: checkly-check-results-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Checks API from Checkly — 18 operation(s) for checks.
  name: Checkly Checks API
  phrasing_intents:
  - id: getV1Checks
    intent: List checks with legacy project fields
    question: Which checks are in my Checkly account, with the older flat project and logicalId fields?
  - id: postV1Checks
    intent: Create an API or browser check (deprecated)
    question: Is the generic create-a-check endpoint that takes either an API or browser type still usable?
  - id: postV1ChecksApi
    intent: Create an API check
    question: How do I set up a new API check that monitors an HTTP endpoint?
  - id: putV1ChecksApiId
    intent: Update an API check
    question: Can I change the request or response time limits on an existing API check?
  - id: postV1ChecksBrowser
    intent: Create a browser check
    question: How can I monitor a web page with a Playwright script in Checkly?
  - id: putV1ChecksBrowserId
    intent: Update a browser check
    question: Can I replace the script of an existing browser check?
  - id: postV1ChecksDns
    intent: Create a DNS monitor
    question: How do I monitor that a domain's DNS records resolve correctly?
  - id: postV1ChecksMultistep
    intent: Create a multi-step check
    question: Can I chain several API calls into a single scripted check?
  phrasing_ops: 18
  slug: checkly-checks-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Dashboards API from Checkly — 5 operation(s) for dashboards.
  name: Checkly Dashboards API
  phrasing_intents:
  - id: getV1Dashboards
    intent: List dashboards
    question: Which public dashboards have I created in Checkly?
  - id: postV1Dashboards
    intent: Create a dashboard
    question: How do I publish a dashboard showing only checks with certain tags?
  - id: deleteV1DashboardsDashboardid
    intent: Delete a dashboard
    question: How do I take down a dashboard permanently?
  - id: getV1DashboardsDashboardid
    intent: Get a dashboard
    question: What tags and display settings does a specific dashboard use?
  - id: putV1DashboardsDashboardid
    intent: Update a dashboard
    question: Can I make an existing dashboard private?
  phrasing_ops: 5
  slug: checkly-dashboards-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Heartbeats API from Checkly — 5 operation(s) for heartbeats.
  name: Checkly Heartbeats API
  phrasing_intents:
  - id: postV1ChecksHeartbeat
    intent: Create a heartbeat check
    question: How do I monitor a cron job that should ping a URL on a schedule?
  - id: putV1ChecksHeartbeatId
    intent: Update a heartbeat check
    question: How do I change the expected period or grace time of an existing heartbeat?
  - id: getV1ChecksHeartbeatsCheckidAvailability
    intent: Get a heartbeat's availability
    question: What percentage of expected pings did my heartbeat receive?
  - id: getV1ChecksHeartbeatsCheckidEvents
    intent: List ping events for a heartbeat
    question: When did my heartbeat last receive a ping?
  - id: getV1ChecksHeartbeatsCheckidEventsId
    intent: Get one heartbeat event
    question: What details are recorded for a single heartbeat ping event?
  phrasing_ops: 5
  slug: checkly-heartbeats-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Incidents API from Checkly — 4 operation(s) for incidents.
  name: Checkly Incidents API
  phrasing_intents:
  - id: postV1Incidents
    intent: Open an incident on a dashboard
    question: How do I announce an incident on one of my dashboards?
  - id: deleteV1IncidentsId
    intent: Delete a dashboard incident
    question: How do I remove a dashboard incident and all its updates?
  - id: getV1IncidentsId
    intent: Get a dashboard incident
    question: What's the current state of a dashboard incident?
  - id: putV1IncidentsId
    intent: Update a dashboard incident
    question: How do I mark a dashboard incident as stopped?
  phrasing_ops: 4
  slug: checkly-incidents-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Maintenance Windows API from Checkly — 12 operation(s) for maintenance windows.
  name: Checkly Maintenance Windows API
  phrasing_intents:
  - id: getV1Maintenancewindows
    intent: List maintenance windows
    question: What maintenance windows are scheduled in my Checkly account?
  - id: postV1Maintenancewindows
    intent: Schedule a maintenance window
    question: How do I pause alerts during a planned deploy window?
  - id: deleteV1MaintenancewindowsId
    intent: Delete a maintenance window
    question: How do I remove a maintenance window I no longer need?
  - id: getV1MaintenancewindowsId
    intent: Get a maintenance window's details
    question: Which checks does a specific maintenance window cover?
  - id: putV1MaintenancewindowsId
    intent: Change a maintenance window
    question: Can I extend an existing maintenance window's end date?
  - id: getV1MaintenancewindowsIdMaintenances
    intent: List occurrences of a maintenance window
    question: What individual maintenances has a recurring window produced?
  - id: deleteV1MaintenancewindowsIdMaintenancesMaintenanceid
    intent: Cancel one occurrence of a maintenance window
    question: Can I skip just one occurrence of a recurring maintenance window?
  - id: getV1MaintenancewindowsIdMaintenancesMaintenanceid
    intent: Get one occurrence of a maintenance window
    question: When does one specific occurrence of my recurring maintenance start?
  phrasing_ops: 12
  slug: checkly-maintenance-windows-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Private Locations API from Checkly — 8 operation(s) for private locations.
  name: Checkly Private Locations API
  phrasing_intents:
  - id: getV1Privatelocations
    intent: List private locations
    question: Which private locations have I set up to run checks inside my network?
  - id: postV1Privatelocations
    intent: Create a private location
    question: How do I run checks from inside my own infrastructure?
  - id: deleteV1PrivatelocationsId
    intent: Remove a private location
    question: How do I decommission a private location I no longer use?
  - id: getV1PrivatelocationsId
    intent: Get a private location
    question: What are the details and keys of a specific private location?
  - id: putV1PrivatelocationsId
    intent: Update a private location
    question: Can I rename a private location or change its proxy?
  - id: postV1PrivatelocationsIdKeys
    intent: Generate an API key for a private location
    question: How do I get a new key for my private location agent?
  - id: deleteV1PrivatelocationsIdKeysKeyid
    intent: Revoke a private location API key
    question: How do I revoke a leaked private location key?
  - id: getV1PrivatelocationsIdMetrics
    intent: Get health metrics for a private location
    question: Is my private location healthy over the last few days?
  phrasing_ops: 8
  slug: checkly-private-locations-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Alert notifications API from Checkly — 1 operation(s) for alert notifications.
  name: Checkly Alert notifications API
  phrasing_intents:
  - id: getV1Alertnotifications
    intent: List sent alert notifications
    question: Did my alert notifications actually get delivered?
  phrasing_ops: 1
  slug: checkly-alert-notifications-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Badges API from Checkly — 2 operation(s) for badges.
  name: Checkly Badges API
  phrasing_intents:
  - id: getV1BadgesChecksCheckid
    intent: Get a status badge for a check
    question: How do I embed a live status badge for one check in my README?
  - id: getV1BadgesGroupsGroupid
    intent: Get a status badge for a check group
    question: Can I show one badge for the overall status of a check group?
  phrasing_ops: 2
  slug: checkly-badges-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Check sessions API from Checkly — 7 operation(s) for check sessions.
  name: Checkly Check sessions API
  phrasing_intents:
  - id: postV1ChecksessionsTrigger
    intent: Trigger check sessions (v1)
    question: How do I kick off my checks on demand from CI with the v1 endpoint?
  - id: getV1ChecksessionsChecksessionid
    intent: Get a check session (v1)
    question: What results has a v1 check session produced so far?
  - id: postV1ChecksessionsChecksessionidCancel
    intent: Cancel a running check session
    question: How do I stop a Playwright check suite run that's still in progress?
  - id: getV1ChecksessionsChecksessionidCompletion
    intent: Wait for a check session to finish (v1)
    question: How can my pipeline block until a v1 check session passes or fails?
  - id: postV2ChecksessionsTrigger
    intent: Trigger check sessions (v2)
    question: How do I trigger check sessions with the newer v2 endpoint?
  - id: getV2ChecksessionsChecksessionid
    intent: Get a check session (v2)
    question: How do I read a check session's results using the v2 endpoint?
  - id: getV2ChecksessionsChecksessionidCompletion
    intent: Wait for a check session to finish (v2)
    question: Does the v2 completion wait also return when a session is degraded or cancelled?
  phrasing_ops: 7
  slug: checkly-check-sessions-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Check status API from Checkly — 2 operation(s) for check status.
  name: Checkly Check status API
  phrasing_intents:
  - id: getV1Checkstatuses
    intent: List the current status of all checks
    question: Which of my checks are currently failing or degraded?
  - id: getV1CheckstatusesCheckid
    intent: Get the current status of a check
    question: Is a specific check passing right now?
  phrasing_ops: 2
  slug: checkly-check-status-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Deployment Triggers API from Checkly — 2 operation(s) for deployment triggers.
  name: Checkly Deployment Triggers API
  phrasing_intents:
  - id: getV1Deploymenttriggers
    intent: List deployment triggers
    question: Which checks run automatically after my GitHub deployments?
  - id: postV1Deploymenttriggers
    intent: Run a check after each GitHub deployment
    question: How do I run my checks against a preview URL every time GitHub deploys?
  phrasing_ops: 2
  slug: checkly-deployment-triggers-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Environment variables API from Checkly — 5 operation(s) for environment variables.
  name: Checkly Environment variables API
  phrasing_intents:
  - id: getV1Variables
    intent: List environment variables
    question: Which account-level environment variables do I have defined?
  - id: postV1Variables
    intent: Create an environment variable
    question: How do I add a new environment variable that my checks can use?
  - id: deleteV1VariablesKey
    intent: Delete an environment variable
    question: How do I remove an environment variable I no longer use?
  - id: getV1VariablesKey
    intent: Get an environment variable
    question: What is the current value and settings of a specific environment variable?
  - id: putV1VariablesKey
    intent: Change an environment variable's value
    question: Can I change the value of an existing environment variable?
  phrasing_ops: 5
  slug: checkly-environment-variables-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Error Groups API from Checkly — 4 operation(s) for error groups.
  name: Checkly Error Groups API
  phrasing_intents:
  - id: getV1Errorgroups
    intent: List error groups across my account
    question: Which recurring errors are my checks hitting across the whole account?
  - id: getV1ErrorgroupsChecksCheckid
    intent: List error groups for one check
    question: What distinct errors has a specific check been failing with?
  - id: getV1ErrorgroupsId
    intent: Get an error group
    question: What are the details of one error group?
  - id: patchV1ErrorgroupsId
    intent: Archive an error group
    question: How do I archive an error group so it stops cluttering my list?
  phrasing_ops: 4
  slug: checkly-error-groups-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Incident Updates API from Checkly — 3 operation(s) for incident updates.
  name: Checkly Incident Updates API
  phrasing_intents:
  - id: postV1IncidentsIncidentidUpdates
    intent: Post an update on a dashboard incident
    question: How do I tell dashboard viewers we've identified the cause of an incident?
  - id: deleteV1IncidentsIncidentidUpdatesId
    intent: Delete a dashboard incident update
    question: How do I remove a single update from a dashboard incident?
  - id: putV1IncidentsIncidentidUpdatesId
    intent: Edit a dashboard incident update
    question: Can I reword an update I already posted on a dashboard incident?
  phrasing_ops: 3
  slug: checkly-incident-updates-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Location API from Checkly — 1 operation(s) for location.
  name: Checkly Location API
  phrasing_intents:
  - id: getV1Locations
    intent: List supported check locations
    question: Which locations can I run my checks from?
  phrasing_ops: 1
  slug: checkly-location-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Monitors API from Checkly — 7 operation(s) for monitors.
  name: Checkly Monitors API
  phrasing_intents:
  - id: putV1ChecksDnsId
    intent: Update a DNS monitor
    question: Can I change the record or domain an existing DNS monitor looks up?
  - id: postV1ChecksIcmp
    intent: Create an ICMP ping monitor
    question: How do I ping a host regularly to see if it's reachable?
  - id: putV1ChecksIcmpId
    intent: Update an ICMP ping monitor
    question: Can I adjust the packet loss thresholds on an existing ping monitor?
  - id: postV1ChecksSsl
    intent: Create an SSL certificate monitor
    question: How can I be warned before my site's SSL certificate has problems?
  - id: putV1ChecksSslId
    intent: Update an SSL certificate monitor
    question: Can I change which host an existing SSL monitor inspects?
  - id: postV1ChecksUrl
    intent: Create a URL uptime monitor
    question: How do I monitor that a web address stays up?
  - id: putV1ChecksUrlId
    intent: Update a URL uptime monitor
    question: Can I change the address an existing URL monitor watches?
  phrasing_ops: 7
  slug: checkly-monitors-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Reporting API from Checkly — 1 operation(s) for reporting.
  name: Checkly Reporting API
  phrasing_intents:
  - id: getV1Reporting
    intent: Report aggregate stats for checks
    question: What was the availability of all my checks last month?
  phrasing_ops: 1
  slug: checkly-reporting-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Rocky AI API from Checkly — 3 operation(s) for rocky ai.
  name: Checkly Rocky AI API
  phrasing_intents:
  - id: postV1RootcauseanalysesErrorgroupsErrorgroupid
    intent: Start a root cause analysis for a check error
    question: Can AI explain the root cause of a recurring check error?
  - id: postV1RootcauseanalysesTestsessionerrorgroupsTestsessionerrorgroupid
    intent: Start a root cause analysis for a test session error
    question: Can AI diagnose why a test session keeps failing with the same error?
  - id: getV1RootcauseanalysesId
    intent: Get a root cause analysis result
    question: Is my root cause analysis finished yet, and what did it find?
  phrasing_ops: 3
  slug: checkly-rocky-ai-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Runtimes API from Checkly — 2 operation(s) for runtimes.
  name: Checkly Runtimes API
  phrasing_intents:
  - id: getV1Runtimes
    intent: List supported runtimes
    question: Which runtimes can my browser checks and setup scripts use?
  - id: getV1RuntimesId
    intent: Get a runtime's packages and versions
    question: Which package versions ship in a specific runtime?
  phrasing_ops: 2
  slug: checkly-runtimes-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Secret scans API from Checkly — 1 operation(s) for secret scans.
  name: Checkly Secret scans API
  phrasing_intents:
  - id: getV1Secretscans
    intent: Find credentials stored inline in config
    question: Are there any API keys or passwords sitting in plain text in my checks or snippets?
  phrasing_ops: 1
  slug: checkly-secret-scans-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Snippets API from Checkly — 5 operation(s) for snippets.
  name: Checkly Snippets API
  phrasing_intents:
  - id: getV1Snippets
    intent: List code snippets
    question: Which reusable code snippets exist in my account?
  - id: postV1Snippets
    intent: Create a code snippet
    question: How do I save a reusable script to share across checks?
  - id: deleteV1SnippetsId
    intent: Delete a code snippet
    question: How do I remove a snippet I no longer need?
  - id: getV1SnippetsId
    intent: Get a code snippet
    question: What code is in a specific snippet?
  - id: putV1SnippetsId
    intent: Update a code snippet
    question: Can I edit the code of an existing snippet?
  phrasing_ops: 5
  slug: checkly-snippets-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Static IPs API from Checkly — 6 operation(s) for static ips.
  name: Checkly Static IPs API
  phrasing_intents:
  - id: getV1Staticips
    intent: List IPv4 addresses checks run from
    question: Which IPv4 addresses do check runs come from so I can allowlist them?
  - id: getV1Staticipsbyregion
    intent: List IPv4 addresses grouped by region
    question: What source IPv4 addresses are used in each region?
  - id: getV1Staticipstxt
    intent: Download IPv4 addresses as a text file
    question: Is there a plain text list of source IPv4 addresses, one per line?
  - id: getV1Staticipv6s
    intent: List IPv6 addresses checks run from
    question: Which IPv6 addresses do check runs use?
  - id: getV1Staticipv6sbyregion
    intent: List IPv6 addresses by region
    question: What IPv6 address does each region use for checks?
  - id: getV1Staticipv6stxt
    intent: Download IPv6 addresses as a text file
    question: Is there a text file of source IPv6 addresses with one per line?
  phrasing_ops: 6
  slug: checkly-static-ips-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Page Incidents API from Checkly — 10 operation(s) for status page incidents.
  name: Checkly Status Page Incidents API
  phrasing_intents:
  - id: getV1StatuspagesIncidents
    intent: List recent status page incidents
    question: What are the latest incidents posted across my status page services?
  - id: postV1StatuspagesIncidents
    intent: Open a status page incident
    question: How do I declare an outage on my status page for specific services?
  - id: deleteV1StatuspagesIncidentsIncidentid
    intent: Delete a status page incident
    question: How do I remove a status page incident and all its updates?
  - id: getV1StatuspagesIncidentsIncidentid
    intent: Get a status page incident
    question: Which services did a specific status page incident affect?
  - id: putV1StatuspagesIncidentsIncidentid
    intent: Edit a status page incident
    question: Can I raise the severity of a status page incident that's already open?
  - id: getV1StatuspagesIncidentsIncidentidIncidentupdates
    intent: List updates on a status page incident
    question: What updates have been posted on one status page incident?
  - id: postV1StatuspagesIncidentsIncidentidIncidentupdates
    intent: Post an update on a status page incident
    question: How do I post progress on a status page incident and notify subscribers?
  - id: deleteV1StatuspagesIncidentsIncidentidIncidentupdatesIncidentupdateid
    intent: Delete a status page incident update
    question: How do I remove one wrong update from a status page incident?
  phrasing_ops: 10
  slug: checkly-status-page-incidents-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Page Services API from Checkly — 5 operation(s) for status page services.
  name: Checkly Status Page Services API
  phrasing_intents:
  - id: getV1StatuspagesServices
    intent: List status page services
    question: Which services are defined for my status pages?
  - id: postV1StatuspagesServices
    intent: Create a status page service
    question: How do I add a new service that incidents can be reported against?
  - id: deleteV1StatuspagesServicesServiceid
    intent: Delete a status page service
    question: How do I remove a service from my status pages?
  - id: getV1StatuspagesServicesServiceid
    intent: Get a status page service
    question: What are the details of one status page service?
  - id: putV1StatuspagesServicesServiceid
    intent: Rename a status page service
    question: How do I rename a service shown on my status page?
  phrasing_ops: 5
  slug: checkly-status-page-services-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Pages API from Checkly — 8 operation(s) for status pages.
  name: Checkly Status Pages API
  phrasing_intents:
  - id: getV1Statuspages
    intent: List status pages
    question: Which status pages exist in my account?
  - id: postV1Statuspages
    intent: Create a status page
    question: How do I publish a new public status page?
  - id: deleteV1StatuspagesStatuspageid
    intent: Delete a status page
    question: How do I take down a status page I no longer need?
  - id: getV1StatuspagesStatuspageid
    intent: Get a status page with cards (deprecated)
    question: What cards and services are on one of my status pages?
  - id: putV1StatuspagesStatuspageid
    intent: Update a status page
    question: Can I change the name, URL or theme of an existing status page?
  - id: getV1StatuspagesStatuspageidSubscriptions
    intent: List a status page's subscriptions
    question: Who is subscribed to updates from a given status page?
  - id: postV1StatuspagesStatuspageidSubscriptionsBulk
    intent: Bulk add subscribers to a status page
    question: Can I import many subscribers onto a status page in one go?
  - id: deleteV1StatuspagesStatuspageidSubscriptionsSubscriptionid
    intent: Remove a subscription from a status page
    question: How do I unsubscribe someone from a status page?
  phrasing_ops: 8
  slug: checkly-status-pages-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Pages V3 API from Checkly — 7 operation(s) for status pages v3.
  name: Checkly Status Pages V3 API
  phrasing_intents:
  - id: listStatusPagesV3Public
    intent: List v3 status pages
    question: Which components-based status pages do I have in Checkly?
  - id: createStatusPageV3Public
    intent: Create a v3 status page
    question: How do I set up a new public status page for my service?
  - id: deleteStatusPageV3Public
    intent: Delete a v3 status page
    question: Does deleting a v3 status page also remove its components and automation rules?
  - id: getStatusPageV3Public
    intent: Get a v3 status page
    question: What branding and domain settings does a given v3 status page have?
  - id: updateStatusPageV3Public
    intent: Replace a v3 status page's settings
    question: Will updating a v3 status page reset fields I leave out?
  - id: getStatusPageV3CustomDomainVerificationPublic
    intent: Get DNS records to verify a status page domain
    question: Which DNS records do I need to add to verify my status page's custom domain?
  - id: recheckStatusPageV3CustomDomainVerificationPublic
    intent: Re-check a status page's custom domain
    question: I just added the DNS records, how do I make it re-verify my status page domain?
  phrasing_ops: 7
  slug: checkly-status-pages-v3-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Pages V3 Automation Rules API from Checkly — 5 operation(s) for status pages v3 automation rules.
  name: Checkly Status Pages V3 Automation Rules API
  phrasing_intents:
  - id: listStatusPageV3AutomationRulesPublic
    intent: List a status page's automation rules
    question: Which automation rules open incidents on my status page?
  - id: createStatusPageV3AutomationRulePublic
    intent: Create an incident automation rule
    question: How can failing checks automatically open an incident on my status page?
  - id: deleteStatusPageV3AutomationRulePublic
    intent: Delete an automation rule
    question: How do I stop a rule from opening incidents automatically?
  - id: getStatusPageV3AutomationRulePublic
    intent: Get an automation rule
    question: What tags and components does a specific automation rule use?
  - id: updateStatusPageV3AutomationRulePublic
    intent: Update an automation rule
    question: Can I change the tags or components of an existing automation rule?
  phrasing_ops: 5
  slug: checkly-status-pages-v3-automation-rules-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Pages V3 Components API from Checkly — 5 operation(s) for status pages v3 components.
  name: Checkly Status Pages V3 Components API
  phrasing_intents:
  - id: listStatusPageV3ComponentsPublic
    intent: List components on a v3 status page
    question: Which components appear on my status page and in what order?
  - id: createStatusPageV3ComponentPublic
    intent: Add a component to a v3 status page
    question: How do I add a service or group component to my status page?
  - id: deleteStatusPageV3ComponentPublic
    intent: Delete a v3 status page component
    question: What happens to child components when I delete a group component?
  - id: getStatusPageV3ComponentPublic
    intent: Get a v3 status page component
    question: What are the settings of one component on my status page?
  - id: updateStatusPageV3ComponentPublic
    intent: Replace a v3 status page component
    question: Will fields I omit be reset when I update a status page component?
  phrasing_ops: 5
  slug: checkly-status-pages-v3-components-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Pages V3 Incidents API from Checkly — 11 operation(s) for status pages v3 incidents.
  name: Checkly Status Pages V3 Incidents API
  phrasing_intents:
  - id: listStatusPageV3IncidentsPublic
    intent: List incidents on a status page
    question: Which incidents are on my status page, most recently updated first?
  - id: createStatusPageV3IncidentPublic
    intent: Open an incident on a status page
    question: How do I declare an outage on my status page?
  - id: deleteStatusPageV3IncidentPublic
    intent: Delete an incident from a status page
    question: How do I remove an incident posted by mistake from my status page?
  - id: getStatusPageV3IncidentPublic
    intent: Get an incident on a status page
    question: What updates and component impacts does a specific incident have?
  - id: updateStatusPageV3IncidentPublic
    intent: Rename an incident or set component status
    question: Can I rename an incident that's already open on my status page?
  - id: replaceStatusPageV3IncidentComponentImpactsPublic
    intent: Rewrite an incident's component impact timeline
    question: Can I retroactively correct when each component was impacted during an incident?
  - id: listStatusPageV3IncidentUpdatesPublic
    intent: List the updates posted to an incident
    question: What progress updates have been posted on an incident so far?
  - id: createStatusPageV3IncidentUpdatePublic
    intent: Post a progress update to an incident
    question: How do I post a status update to an ongoing incident?
  phrasing_ops: 11
  slug: checkly-status-pages-v3-incidents-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Status Pages V3 Subscribers API from Checkly — 3 operation(s) for status pages v3 subscribers.
  name: Checkly Status Pages V3 Subscribers API
  phrasing_intents:
  - id: listStatusPageV3SubscribersPublic
    intent: List subscribers of a v3 status page
    question: Who has subscribed to email updates from my status page?
  - id: bulkCreateStatusPageV3SubscribersPublic
    intent: Bulk-subscribe emails to a v3 status page
    question: How do I import a list of customer emails as status page subscribers?
  - id: deleteStatusPageV3SubscriberPublic
    intent: Remove a status page subscriber
    question: How do I unsubscribe someone from my status page?
  phrasing_ops: 3
  slug: checkly-status-pages-v3-subscribers-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Subscriptions API from Checkly — 3 operation(s) for subscriptions.
  name: Checkly Subscriptions API
  phrasing_intents:
  - id: getV1StatuspagesStatuspageidSubscriptions
    intent: List subscribers of a status page
    question: Which email subscribers are signed up to my status page?
  - id: postV1StatuspagesStatuspageidSubscriptionsBulk
    intent: Import subscribers onto a status page
    question: Can I import a list of subscribers onto a status page at once?
  - id: deleteV1StatuspagesStatuspageidSubscriptionsSubscriptionid
    intent: Delete a status page subscription
    question: How do I remove one subscriber from a status page?
  phrasing_ops: 3
  slug: checkly-subscriptions-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Test Session Error Groups API from Checkly — 4 operation(s) for test session error groups.
  name: Checkly Test Session Error Groups API
  phrasing_intents:
  - id: getV1Testsessionerrorgroups
    intent: List test session error groups
    question: Which recurring errors show up across my test sessions?
  - id: getV1TestsessionerrorgroupsProjectsProjectid
    intent: List test session error groups for a project
    question: What test session errors is a specific project hitting?
  - id: getV1TestsessionerrorgroupsId
    intent: Get a test session error group
    question: What are the details of one test session error group?
  - id: patchV1TestsessionerrorgroupsId
    intent: Archive a test session error group
    question: How do I archive a test session error group?
  phrasing_ops: 4
  slug: checkly-test-session-error-groups-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Test sessions API from Checkly — 7 operation(s) for test sessions.
  name: Checkly Test sessions API
  phrasing_intents:
  - id: getV1Testsessions
    intent: List test sessions
    question: Which test sessions ran recently in my account?
  - id: postV1TestsessionsTrigger
    intent: Start a test session
    question: How do I launch a test session against my checks with extra environment variables?
  - id: getV1TestsessionsTestsessionid
    intent: Get a test session
    question: What's the current state and results of a test session?
  - id: postV1TestsessionsTestsessionidCancel
    intent: Cancel a running test session
    question: How do I stop a test session that's still running?
  - id: getV1TestsessionsTestsessionidCompletion
    intent: Wait for a test session to finish
    question: Can I block until a test session passes or fails?
  - id: getV1TestsessionsTestsessionidResultsTestsessionresultid
    intent: Get one result from a test session
    question: What are the details of a single result inside a test session?
  - id: getV1TestsessionsTestsessionidResultsTestsessionresultidAssets
    intent: List downloadable assets of a test session result
    question: Where can I download the traces, screenshots or videos from a test session result?
  phrasing_ops: 7
  slug: checkly-test-sessions-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Triggers API from Checkly — 9 operation(s) for triggers.
  name: Checkly Triggers API
  phrasing_intents:
  - id: postV1ChecksessionsTrigger
    intent: Start check sessions for matching checks (v1)
    question: How do I run my checks on demand right now through the original v1 trigger?
  - id: postV1TestsessionsTrigger
    intent: Trigger a test session
    question: Can I kick off a named test run of my checks from a chosen location?
  - id: deleteV1TriggersCheckgroupsGroupid
    intent: Delete a check group trigger (deprecated)
    question: How do I remove the trigger from a check group?
  - id: getV1TriggersCheckgroupsGroupid
    intent: Get a check group's trigger URL (deprecated)
    question: What is the deprecated trigger URL for one of my check groups?
  - id: postV1TriggersCheckgroupsGroupid
    intent: Create a check group trigger (deprecated)
    question: Can I create a URL that runs a whole check group when called?
  - id: deleteV1TriggersChecksCheckid
    intent: Delete a check trigger (deprecated)
    question: How do I remove a single check's trigger?
  - id: getV1TriggersChecksCheckid
    intent: Get a check's trigger URL (deprecated)
    question: What is the trigger URL for a single check?
  - id: postV1TriggersChecksCheckid
    intent: Create a check trigger (deprecated)
    question: Can I get a URL that runs one specific check when called?
  phrasing_ops: 9
  slug: checkly-triggers-api
- baseURL: https://api.checklyhq.com
  baseurl_source: declared
  description: The Clientcertificates API from Checkly — 2 operation(s) for clientcertificates.
  name: Checkly Clientcertificates API
  phrasing_intents:
  - id: getV1Clientcertificates
    intent: List client certificates
    question: Which client certificates have I uploaded for mTLS checks?
  - id: postV1Clientcertificates
    intent: Upload a client certificate
    question: How do I let my API checks call an endpoint that requires mutual TLS?
  - id: deleteV1ClientcertificatesId
    intent: Delete a client certificate
    question: How do I remove an expired client certificate?
  - id: getV1ClientcertificatesId
    intent: Get a client certificate
    question: What host is a specific client certificate registered for?
  phrasing_ops: 4
  slug: checkly-clientcertificates-api
artifact_total: 74
asyncapis:
- description: ''
  name: Checkly Webhooks
  slug: checkly-webhooks
collections:
- collection_type: open
  name: Checkly Public Accounts API
  slug: open-checkly-accounts-api
- collection_type: open
  name: Checkly Public Accounts Alert Channels API
  slug: open-checkly-alert-channels-api
- collection_type: open
  name: Checkly Public Accounts Analytics API
  slug: open-checkly-analytics-api
- collection_type: open
  name: Checkly Public Accounts Check Alerts API
  slug: open-checkly-check-alerts-api
- collection_type: open
  name: Checkly Public Accounts Check Groups API
  slug: open-checkly-check-groups-api
- collection_type: open
  name: Checkly Public Accounts Check Results API
  slug: open-checkly-check-results-api
- collection_type: open
  name: Checkly Public Accounts Check Statuses API
  slug: open-checkly-check-statuses-api
- collection_type: open
  name: Checkly Public Accounts Checks API
  slug: open-checkly-checks-api
- collection_type: open
  name: Checkly Public Accounts Dashboards API
  slug: open-checkly-dashboards-api
- collection_type: open
  name: Checkly Public Accounts Heartbeats API
  slug: open-checkly-heartbeats-api
- collection_type: open
  name: Checkly Public Accounts Incidents API
  slug: open-checkly-incidents-api
- collection_type: open
  name: Checkly Public Accounts Locations API
  slug: open-checkly-locations-api
- collection_type: open
  name: Checkly Public Accounts Maintenance Windows API
  slug: open-checkly-maintenance-windows-api
- collection_type: open
  name: Checkly Public Accounts Private Locations API
  slug: open-checkly-private-locations-api
- collection_type: open
  name: Checkly Public Accounts Reports API
  slug: open-checkly-reports-api
- collection_type: open
  name: Checkly Public Accounts Variables API
  slug: open-checkly-variables-api
- collection_type: open
  name: Checkly Public API
  slug: open-checkly
common:
- group: other
  href: https://artifacts.apis.io/checkly/capabilities/checkly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/checkly-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/checkly/checkly-cli/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/checkly/agentic-access/checkly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/checkly-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/checkly/security/checkly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/checkly-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/checkly/security/checkly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/checkly-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/checkly/authentication/checkly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/checkly-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/checkly/checkly-cli
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/checkly
- group: company
  title: ''
  type: Website
  url: https://www.checklyhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.checklyhq.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/checkly
- group: company
  title: ''
  type: Blog
  url: https://www.checklyhq.com/blog/feed
- group: build
  href: https://artifacts.apis.io/checkly/packages/checkly-packages.yml
  title: ''
  type: Packages
  url: packages/checkly-packages.yml
- group: build
  href: https://artifacts.apis.io/checkly/packages/checkly-packages.yml
  title: ''
  type: SDKs
  url: packages/checkly-packages.yml
- group: build
  href: https://artifacts.apis.io/checkly/cli/checkly-cli.yml
  title: ''
  type: CLI
  url: cli/checkly-cli.yml
- group: agent
  href: https://artifacts.apis.io/checkly/well-known/checkly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/checkly-well-known.yml
- group: auth
  href: https://artifacts.apis.io/checkly/well-known/checkly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/checkly-security.txt
- group: agent
  href: https://artifacts.apis.io/checkly/mcp/checkly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/checkly-mcp.yml
- group: build
  href: https://artifacts.apis.io/checkly/mcp/checkly-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/checkly-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/checkly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/checkly/llms/checkly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/checkly-llms.txt
- group: other
  href: https://artifacts.apis.io/checkly/overlays/checkly-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/checkly-public-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/checkly/conformance/checkly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/checkly-conformance.yml
- group: auth
  href: https://artifacts.apis.io/checkly/conformance/checkly-conformance.yml
  title: ''
  type: Compliance
  url: conformance/checkly-conformance.yml
- group: design
  href: https://artifacts.apis.io/checkly/errors/checkly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/checkly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/checkly/lifecycle/checkly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/checkly-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/checkly/lifecycle/checkly-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/checkly-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://is.checkly.online/
- group: auth
  href: https://artifacts.apis.io/checkly/scopes/checkly-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/checkly-scopes.yml
- group: design
  href: https://artifacts.apis.io/checkly/conventions/checkly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/checkly-conventions.yml
- group: operate
  href: https://artifacts.apis.io/checkly/changelog/checkly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/checkly-changelog.yml
- group: design
  href: https://artifacts.apis.io/checkly/data-model/checkly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/checkly-data-model.yml
- group: design
  href: https://artifacts.apis.io/checkly/asyncapi/checkly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/checkly-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/checkly/plans/checkly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/checkly-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/checkly/rate-limits/checkly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/checkly-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/checkly/security/checkly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/checkly-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/checkly/security/checkly-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/checkly-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/checkly/finops/checkly-finops.yml
  title: ''
  type: FinOps
  url: finops/checkly-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.checklyhq.com/docs/api-reference/overview/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.checklyhq.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.checklyhq.com/docs/what-is-checkly/
- group: start
  title: ''
  type: Quickstart
  url: https://www.checklyhq.com/docs/cli/installation/
- group: operate
  title: ''
  type: Support
  url: https://www.checklyhq.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.checklyhq.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.checklyhq.com/signup/
- group: start
  title: ''
  type: Login
  url: https://app.checklyhq.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.checklyhq.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.checklyhq.com/privacy/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.checklyhq.com/roadmap/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/checkly/checkly-cli
created: '2026-03-25'
description: 'Checkly is a code-first reliability platform for synthetic monitoring, uptime monitoring, alerting and AI-assisted incident investigation. Engineering teams define monitors as versioned code with the Checkly CLI, Terraform or Pulumi, reuse existing Playwright suites as production browser checks, and run them from 22 global locations or from private locations inside their own network. The platform spans three modules: Detect (uptime, API and browser monitoring), Communicate (alerting, status pages and dashboards) and Resolve (OpenTelemetry tracing and Rocky AI root cause analysis). Checkly exposes a 225-operation public REST API, a hosted MCP server, four published Agent Skills and machine-readable llms.txt, docs and pricing.'
finops:
- has_sources: true
  method: derived
  name: Checkly Finops
  primary_unit: account
  service_category: ''
  slug: checkly-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/checkly.png
layout: provider
mcp_servers:
- description: Hosted, remote MCP server that lets an agent inspect Checkly checks, check results and test sessions, fetch result assets, read and trigger Rocky AI root cause analyses, manage account environment var
  name: Checkly MCP Server
  slug: checkly-mcp-server
modified: '2026-08-29'
name: Checkly
nav: Providers
network: true
overview: 'Checkly publishes 42 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Alert Channels API, Analytics API, and 39 more. Tagged areas include Monitoring, Testing, Synthetic Monitoring, Observability, and Uptime.


  The Checkly catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Checkly''s developer surface includes authentication, documentation, engineering blog, CLI, changelog, API reference, getting-started guide, and 43 more developer resources.'
plans:
- name: Checkly Plans Pricing
  plan_count: 9
  slug: checkly-plans-pricing
- name: Checkly Price Estimates
  plan_count: 0
  slug: checkly-price-estimates
random_paper: 19
rate_limits:
- limit_count: 2
  name: Checkly Rate Limits
  slug: checkly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Checkly API Rules
  rule_count: 58
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 16
  slug: checkly-rules
scopes:
- name: Checkly Scopes
  scope_count: 14
  slug: checkly-scopes
  summary_line: 14 scopes
score:
  band: exemplar
  composite: 77.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 65.2
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 86.8
  previous_composite: 75.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 41
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/checkly/checkly-2026-06-20T174251.png
security:
- kind: authentication
  name: Checkly Authentication
  slug: checkly-authentication
  summary_line: http/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Checkly Domain Security
  slug: checkly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Checkly Vulnerability Disclosure
  slug: checkly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Checkly Trust Center
  slug: checkly-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 2
skills:
- name: checkly
  slug: checkly-2
- name: checkly
  slug: checkly
slug: checkly
tags:
- Monitoring
- Testing
- Synthetic Monitoring
- Observability
- Uptime
- Alerting
- Status Pages
- Monitoring as Code
- Playwright
- DevOps
website: https://www.checklyhq.com
---
