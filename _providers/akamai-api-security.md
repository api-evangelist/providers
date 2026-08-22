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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 103
  human_in_the_loop: 0
  name: Akamai Api Security Agentic Access
  operation_count: 213
  slug: akamai-api-security-agentic-access
  summary_line: 213 operations · 103 acting
api_count: 65
apis:
- description: Akamai provides a comprehensive set of REST APIs for managing and configuring their platform services, including API security, CDN, edge computing, and security products. The APIs use the Akamai EdgeG
  name: Akamai APIs
  slug: akamai-apis
- description: Get the activation history for a configuration.
  name: Akamai API Security Activation history API
  slug: akamai-api-security-activation-history-api
- description: Get status information about your activations and activation requests.
  name: Akamai API Security Activation status API
  slug: akamai-api-security-activation-status-api
- description: Manage your security configuration activations.
  name: Akamai API Security Activations API
  slug: akamai-api-security-activations-api
- description: Get the list of API endpoints associated with a security policy.
  name: Akamai API Security API endpoints API
  slug: akamai-api-security-api-endpoints-api
- description: Manage API request limits and the actions to take when those limits are met.
  name: Akamai API Security API request constraints API
  slug: akamai-api-security-api-request-constraints-api
- description: Manage the attack payload log settings for your security configurations.
  name: Akamai API Security Attack payload logs API
  slug: akamai-api-security-attack-payload-logs-api
- description: List all hostnames for a given contract and group.
  name: Akamai API Security Available hostnames API
  slug: akamai-api-security-available-hostnames-api
- description: Manage the bypass network lists used with your security policies.
  name: Akamai API Security Bypass network lists API
  slug: akamai-api-security-bypass-network-lists-api
- description: Manage your client reputation profiles.
  name: Akamai API Security Client reputation API
  slug: akamai-api-security-client-reputation-api
- description: The Client-Side Protections & Compliance API from Akamai API Security — 1 operation(s) for client-side protections & compliance.
  name: Akamai API Security Client-Side Protections & Compliance API
  slug: akamai-api-security-client-side-protections-compliance-api
- description: Manage hostnames you're currently evaluating for a configuration version. If using Web Application Protector, manage hostnames currently in evaluation mode. This mode lets you to see how your configur
  name: 'Akamai API Security Configuration: Evaluation hostnames API'
  slug: akamai-api-security-configuration-evaluation-hostnames-api
- description: The Configuration version diff API from Akamai API Security — 1 operation(s) for configuration version diff.
  name: Akamai API Security Configuration version diff API
  slug: akamai-api-security-configuration-version-diff-api
- description: Get comprehensive details about a security configuration version.
  name: Akamai API Security Configuration version export API
  slug: akamai-api-security-configuration-version-export-api
- description: List the contracts and groups for your account.
  name: Akamai API Security Contracts and groups API
  slug: akamai-api-security-contracts-and-groups-api
- description: The Cookie Settings API from Akamai API Security — 1 operation(s) for cookie settings.
  name: Akamai API Security Cookie Settings API
  slug: akamai-api-security-cookie-settings-api
- description: Manage the actions contained in your custom rules. Use custom rules to handle scenarios not covered by the included standard rules or to quickly patch new website vulnerabilities.
  name: Akamai API Security Custom rule actions API
  slug: akamai-api-security-custom-rule-actions-api
- description: See which CVEs are covered by App & API Protector. The catalog contains only CVEs that the Akamai Threat Research team is aware of. App & API Protector can identify and block attacks related to the ac
  name: Akamai API Security CVE Protections lookup API
  slug: akamai-api-security-cve-protections-lookup-api
- description: Get information about APIs discovered in your traffic that are new or not yet protected under API protections.
  name: Akamai API Security Discovered APIs API
  slug: akamai-api-security-discovered-apis-api
- description: Manage the API endpoints associated with a security policy.
  name: Akamai API Security Endpoints API
  slug: akamai-api-security-endpoints-api
- description: Manage the evasive path match for your security configurations.
  name: Akamai API Security Evasive path match API
  slug: akamai-api-security-evasive-path-match-api
- description: Get a list of the failover hostnames in a security configuration.
  name: Akamai API Security Failover hostnames API
  slug: akamai-api-security-failover-hostnames-api
- description: Manage security configurations and their versions.
  name: Akamai API Security General configuration settings API
  slug: akamai-api-security-general-configuration-settings-api
- description: Manage security policies and their versions.
  name: Akamai API Security General policy settings API
  slug: akamai-api-security-general-policy-settings-api
- description: Get the list of hostnames in an account with their current protections, activation statuses, and other summary information.
  name: Akamai API Security Hostname coverage API
  slug: akamai-api-security-hostname-coverage-api
- description: Manage the hostnames in your configuration settings.
  name: Akamai API Security Hostnames API
  slug: akamai-api-security-hostnames-api
- description: Manage the HTTP header log settings for security policies.
  name: Akamai API Security HTTP header logs API
  slug: akamai-api-security-http-header-logs-api
- description: Manage which network lists are used in the IP/Geo Firewall settings. If you want to add or remove IP addresses from the network lists, use the Network Lists API.
  name: Akamai API Security IP/Geo Firewall settings API
  slug: akamai-api-security-ip-geo-firewall-settings-api
- description: Manage the actions taken by your malware policies.
  name: Akamai API Security Malware policy actions API
  slug: akamai-api-security-malware-policy-actions-api
- description: Manage your match targets, which define which security policy applies to an API, hostname, or path.
  name: Akamai API Security Match targets API
  slug: akamai-api-security-match-targets-api
- description: Manage your onboardings' activations, and the activation history for each onboarding.
  name: 'Akamai API Security Onboarding: Activations and status API'
  slug: akamai-api-security-onboarding-activations-and-status-api
- description: Manage onboardings and their settings.
  name: 'Akamai API Security Onboarding: Creation and settings API'
  slug: akamai-api-security-onboarding-creation-and-settings-api
- description: Manage your post activations validations and cname your hostnames to akamai in order to go live.
  name: 'Akamai API Security Onboarding: Post-activation validation API'
  slug: akamai-api-security-onboarding-post-activation-validation-api
- description: Manage settings for Personally Identifiable Information (PII) learning. With this feature, the network discovers PII on your behalf.
  name: Akamai API Security PII learning API
  slug: akamai-api-security-pii-learning-api
- description: Manage the Pragma header settings for your security policies.
  name: Akamai API Security Pragma settings API
  slug: akamai-api-security-pragma-settings-api
- description: Manage your prefetch request protections. When enabled, your application firewall rules inspect internal requests, which are those between your origin and Akamai's servers, for the file types you spec
  name: Akamai API Security Prefetch requests API
  slug: akamai-api-security-prefetch-requests-api
- description: 'Manage various security policy protections. These settings enable or disable each protection on your policy. However, you set the protections themselves in their corresponding operations available in '
  name: Akamai API Security Protections API
  slug: akamai-api-security-protections-api
- description: Manage rate policy actions, which are the actions each policy takes when conditions are met.
  name: Akamai API Security Rate policy actions API
  slug: akamai-api-security-rate-policy-actions-api
- description: If using Kona Site Defender, manage the reputation analysis settings.
  name: Akamai API Security Reputation analysis API
  slug: akamai-api-security-reputation-analysis-api
- description: Manage limits for the maximum request body size allowed.
  name: Akamai API Security Request body inspection limits API
  slug: akamai-api-security-request-body-inspection-limits-api
- description: Manage a security configuration's inspection limit settings for request bodies.
  name: Akamai API Security Request body size API
  slug: akamai-api-security-request-body-size-api
- description: Manage the attack groups and rules that you're currently evaluating for your security policies.
  name: 'Akamai API Security Security policy: Conditions and exceptions API'
  slug: akamai-api-security-security-policy-conditions-and-exceptions-api
- description: Manage the attack groups that you're evaluating for your security configurations and policies.
  name: 'Akamai API Security Security policy: Evaluation attack groups API'
  slug: akamai-api-security-security-policy-evaluation-attack-groups-api
- description: Manage hostnames you're currently evaluating for security policies.
  name: 'Akamai API Security Security policy: Evaluation hostnames API'
  slug: akamai-api-security-security-policy-evaluation-hostnames-api
- description: Set the evaluation mode for your security policies. This mode runs concurrently with your existing Web Application Firewall Rule settings and records how the rules would respond if applied to live tra
  name: 'Akamai API Security Security policy: Evaluation mode API'
  slug: akamai-api-security-security-policy-evaluation-mode-api
- description: Manage the penalty box settings that you're evaluating for your security policies.
  name: 'Akamai API Security Security policy: Evaluation penalty box API'
  slug: akamai-api-security-security-policy-evaluation-penalty-box-api
- description: Manage the rules you're currently evaluating for security policies.
  name: 'Akamai API Security Security policy: Evaluation rules API'
  slug: akamai-api-security-security-policy-evaluation-rules-api
- description: Manage your custom deny actions for security configurations and policies. Custom deny actions let you serve error messages, pages, and responses that meet your organization's unique needs.
  name: 'Akamai API Security Shared resources: Custom deny actions API'
  slug: akamai-api-security-shared-resources-custom-deny-actions-api
- description: Manage your custom rules for security configurations and policies.
  name: 'Akamai API Security Shared resources: Custom rules API'
  slug: akamai-api-security-shared-resources-custom-rules-api
- description: Manage your malware policies.
  name: 'Akamai API Security Shared resources: Malware policies API'
  slug: akamai-api-security-shared-resources-malware-policies-api
- description: Manage rate policies for security configurations.
  name: 'Akamai API Security Shared resources: Rate policies API'
  slug: akamai-api-security-shared-resources-rate-policies-api
- description: Manage your reputation profiles. Reputation protections identify potentially malicious IP addresses, scoring them based on prior interactions with other Akamai customers.
  name: 'Akamai API Security Shared resources: Reputation profiles API'
  slug: akamai-api-security-shared-resources-reputation-profiles-api
- description: Manage SIEM settings for your security configurations.
  name: Akamai API Security SIEM settings API
  slug: akamai-api-security-siem-settings-api
- description: Manage your slow POST protection settings for your security policies.
  name: Akamai API Security Slow POST protections API
  slug: akamai-api-security-slow-post-protections-api
- description: Manage the email subscriptions for features within a specific security configuration.
  name: Akamai API Security Subscriptions API
  slug: akamai-api-security-subscriptions-api
- description: Manage your URL protection policies.
  name: Akamai API Security URL protection policies API
  slug: akamai-api-security-url-protection-policies-api
- description: Manage your URL protection settings for your security policies.
  name: Akamai API Security URL protection policy actions API
  slug: akamai-api-security-url-protection-policy-actions-api
- description: Manage your WAF attack groups.
  name: 'Akamai API Security WAF rules: Attack groups API'
  slug: akamai-api-security-waf-rules-attack-groups-api
- description: Manage the penalty box condition settings for your firewall rules.
  name: 'Akamai API Security WAF rules: Evaluation Penalty box conditions API'
  slug: akamai-api-security-waf-rules-evaluation-penalty-box-conditions-api
- description: Manage your Web Application Firewall (WAF) rules and rule sets.
  name: 'Akamai API Security WAF rules: General settings API'
  slug: akamai-api-security-waf-rules-general-settings-api
- description: Manage the penalty box settings for your Web Application Firewall implementation.
  name: 'Akamai API Security WAF rules: Penalty box API'
  slug: akamai-api-security-waf-rules-penalty-box-api
- description: Manage the conditions used with your Web Application Firewall's penalty box.
  name: 'Akamai API Security WAF rules: Penalty box conditions API'
  slug: akamai-api-security-waf-rules-penalty-box-conditions-api
- description: Quickly manage and mitigate risks resulting from the most recent high-profile, critical vulnerabilities. __Note__. Rapid rules are rules you can apply while we are still testing and perfecting them. O
  name: 'Akamai API Security WAF rules: Rapid rules API'
  slug: akamai-api-security-waf-rules-rapid-rules-api
- description: Manage the tuning recommendations for your WAF attack groups.
  name: 'Akamai API Security WAF rules: Tuning recommendations API'
  slug: akamai-api-security-waf-rules-tuning-recommendations-api
- description: Manage the mode used with your WAF rules. Your mode you set determines how your rule sets are updated.
  name: 'Akamai API Security WAF rules: Update mode API'
  slug: akamai-api-security-waf-rules-update-mode-api
artifact_total: 368
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Akamai: Application Security Activation history API'
  slug: open-akamai-api-security-activation-history-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Activation status API'
  slug: open-akamai-api-security-activation-status-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Activations API'
  slug: open-akamai-api-security-activations-api
- collection_type: open
  name: 'Akamai: Application Security Activation history API endpoints API'
  slug: open-akamai-api-security-api-endpoints-api
- collection_type: open
  name: 'Akamai: Application Security Activation history API request constraints API'
  slug: open-akamai-api-security-api-request-constraints-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Attack payload logs API'
  slug: open-akamai-api-security-attack-payload-logs-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Available hostnames API'
  slug: open-akamai-api-security-available-hostnames-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Bypass network lists API'
  slug: open-akamai-api-security-bypass-network-lists-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Client reputation API'
  slug: open-akamai-api-security-client-reputation-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Client-Side Protections & Compliance API'
  slug: open-akamai-api-security-client-side-protections-compliance-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Configuration: Evaluation hostnames API'
  slug: open-akamai-api-security-configuration-evaluation-hostnames-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Configuration version diff API'
  slug: open-akamai-api-security-configuration-version-diff-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Configuration version export API'
  slug: open-akamai-api-security-configuration-version-export-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Contracts and groups API'
  slug: open-akamai-api-security-contracts-and-groups-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Cookie Settings API'
  slug: open-akamai-api-security-cookie-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Custom rule actions API'
  slug: open-akamai-api-security-custom-rule-actions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history CVE Protections lookup API'
  slug: open-akamai-api-security-cve-protections-lookup-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Discovered APIs API'
  slug: open-akamai-api-security-discovered-apis-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Endpoints API'
  slug: open-akamai-api-security-endpoints-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Evasive path match API'
  slug: open-akamai-api-security-evasive-path-match-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Failover hostnames API'
  slug: open-akamai-api-security-failover-hostnames-api
- collection_type: open
  name: 'Akamai: Application Security Activation history General configuration settings API'
  slug: open-akamai-api-security-general-configuration-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history General policy settings API'
  slug: open-akamai-api-security-general-policy-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Hostname coverage API'
  slug: open-akamai-api-security-hostname-coverage-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Hostnames API'
  slug: open-akamai-api-security-hostnames-api
- collection_type: open
  name: 'Akamai: Application Security Activation history HTTP header logs API'
  slug: open-akamai-api-security-http-header-logs-api
- collection_type: open
  name: 'Akamai: Application Security Activation history IP/Geo Firewall settings API'
  slug: open-akamai-api-security-ip-geo-firewall-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Malware policy actions API'
  slug: open-akamai-api-security-malware-policy-actions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Match targets API'
  slug: open-akamai-api-security-match-targets-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Onboarding: Activations and status API'
  slug: open-akamai-api-security-onboarding-activations-and-status-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Onboarding: Creation and settings API'
  slug: open-akamai-api-security-onboarding-creation-and-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Onboarding: Post-activation validation API'
  slug: open-akamai-api-security-onboarding-post-activation-validation-api
- collection_type: open
  name: 'Akamai: Application Security Activation history PII learning API'
  slug: open-akamai-api-security-pii-learning-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Pragma settings API'
  slug: open-akamai-api-security-pragma-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Prefetch requests API'
  slug: open-akamai-api-security-prefetch-requests-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Protections API'
  slug: open-akamai-api-security-protections-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Rate policy actions API'
  slug: open-akamai-api-security-rate-policy-actions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Reputation analysis API'
  slug: open-akamai-api-security-reputation-analysis-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Request body inspection limits API'
  slug: open-akamai-api-security-request-body-inspection-limits-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Request body size API'
  slug: open-akamai-api-security-request-body-size-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Security policy: Conditions and exceptions API'
  slug: open-akamai-api-security-security-policy-conditions-and-exceptions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Security policy: Evaluation attack groups API'
  slug: open-akamai-api-security-security-policy-evaluation-attack-groups-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Security policy: Evaluation hostnames API'
  slug: open-akamai-api-security-security-policy-evaluation-hostnames-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Security policy: Evaluation mode API'
  slug: open-akamai-api-security-security-policy-evaluation-mode-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Security policy: Evaluation penalty box API'
  slug: open-akamai-api-security-security-policy-evaluation-penalty-box-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Security policy: Evaluation rules API'
  slug: open-akamai-api-security-security-policy-evaluation-rules-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Shared resources: Custom deny actions API'
  slug: open-akamai-api-security-shared-resources-custom-deny-actions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Shared resources: Custom rules API'
  slug: open-akamai-api-security-shared-resources-custom-rules-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Shared resources: Malware policies API'
  slug: open-akamai-api-security-shared-resources-malware-policies-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Shared resources: Rate policies API'
  slug: open-akamai-api-security-shared-resources-rate-policies-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Shared resources: Reputation profiles API'
  slug: open-akamai-api-security-shared-resources-reputation-profiles-api
- collection_type: open
  name: 'Akamai: Application Security Activation history SIEM settings API'
  slug: open-akamai-api-security-siem-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Slow POST protections API'
  slug: open-akamai-api-security-slow-post-protections-api
- collection_type: open
  name: 'Akamai: Application Security Activation history Subscriptions API'
  slug: open-akamai-api-security-subscriptions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history URL protection policies API'
  slug: open-akamai-api-security-url-protection-policies-api
- collection_type: open
  name: 'Akamai: Application Security Activation history URL protection policy actions API'
  slug: open-akamai-api-security-url-protection-policy-actions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: Attack groups API'
  slug: open-akamai-api-security-waf-rules-attack-groups-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: Evaluation Penalty box conditions API'
  slug: open-akamai-api-security-waf-rules-evaluation-penalty-box-conditions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: General settings API'
  slug: open-akamai-api-security-waf-rules-general-settings-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: Penalty box API'
  slug: open-akamai-api-security-waf-rules-penalty-box-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: Penalty box conditions API'
  slug: open-akamai-api-security-waf-rules-penalty-box-conditions-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: Rapid rules API'
  slug: open-akamai-api-security-waf-rules-rapid-rules-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: Tuning recommendations API'
  slug: open-akamai-api-security-waf-rules-tuning-recommendations-api
- collection_type: open
  name: 'Akamai: Application Security Activation history WAF rules: Update mode API'
  slug: open-akamai-api-security-waf-rules-update-mode-api
- collection_type: open
  name: 'Akamai: Application Security API'
  slug: open-akamai-api-security
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akamai-api-security-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akamai-api-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akamai.com/products/api-security
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.akamai.com
- group: company
  title: ''
  type: Blog
  url: https://www.akamai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.akamai.com/products/api-security#pricing
- group: operate
  title: ''
  type: Support
  url: https://www.akamai.com/support
- group: start
  title: ''
  type: Login
  url: https://control.akamai.com
- group: start
  title: ''
  type: Signup
  url: https://www.akamai.com/free-trials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akamai
- group: operate
  title: ''
  type: StatusPage
  url: https://www.akamaistatus.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akamai-technologies
- group: other
  title: ''
  type: X
  url: https://twitter.com/Akamai
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/rules/akamai-api-security-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/vocabulary/akamai-api-security-vocabulary.yaml
created: '2026-03-26'
description: Akamai API Security (formerly Noname Security) provides comprehensive API discovery, posture management, and threat protection for organizations across cloud, on-premises, and hybrid environments. The platform continuously discovers and monitors all APIs, identifies vulnerabilities and misconfigurations, detects and responds to API threats in real time, and provides pre-production security testing integrated into CI/CD pipelines.
examples:
- key_count: 1
  name: Api Security Attack Payload Logging Example
  slug: api-security-attack-payload-logging-example
- key_count: 3
  name: Api Security Attack Payload Logging Get 200 Example
  slug: api-security-attack-payload-logging-get-200-example
- key_count: 3
  name: Api Security Attack Payload Logging Put 200 Example
  slug: api-security-attack-payload-logging-put-200-example
- key_count: 3
  name: Api Security Attack Payload Logging Put Example
  slug: api-security-attack-payload-logging-put-example
- key_count: 1
  name: Api Security Bypass Network Lists Get Example
  slug: api-security-bypass-network-lists-get-example
- key_count: 1
  name: Api Security Bypass Network Lists Put Example
  slug: api-security-bypass-network-lists-put-example
- key_count: 5
  name: Api Security Client Reputation Condition Example
  slug: api-security-client-reputation-condition-example
- key_count: 2
  name: Api Security Config Clone Post Example
  slug: api-security-config-clone-post-example
- key_count: 7
  name: Api Security Config Get Example
  slug: api-security-config-get-example
- key_count: 6
  name: Api Security Config Post Example
  slug: api-security-config-post-example
- key_count: 2
  name: Api Security Config Rename Example
  slug: api-security-config-rename-example
- key_count: 1
  name: Api Security Configs Get Example
  slug: api-security-configs-get-example
- key_count: 2
  name: Api Security Cookie Settings Example
  slug: api-security-cookie-settings-example
- key_count: 1
  name: Api Security Custom Denies Example
  slug: api-security-custom-denies-example
- key_count: 4
  name: Api Security Custom Deny Example
  slug: api-security-custom-deny-example
- key_count: 16
  name: Api Security Custom Rule Example
  slug: api-security-custom-rule-example
- key_count: 1
  name: Api Security Custom Rules Example
  slug: api-security-custom-rules-example
- key_count: 3
  name: Api Security Effective Time Period Example
  slug: api-security-effective-time-period-example
- key_count: 1
  name: Api Security Evasive Path Match Get 200 Example
  slug: api-security-evasive-path-match-get-200-example
- key_count: 1
  name: Api Security Evasive Path Match Put 200 Example
  slug: api-security-evasive-path-match-put-200-example
- key_count: 1
  name: Api Security Evasive Path Match Put Example
  slug: api-security-evasive-path-match-put-example
- key_count: 4
  name: Api Security Header Logging Get 200 Example
  slug: api-security-header-logging-get-200-example
- key_count: 4
  name: Api Security Header Logging Put 200 Example
  slug: api-security-header-logging-put-200-example
- key_count: 4
  name: Api Security Header Logging Put Example
  slug: api-security-header-logging-put-example
- key_count: 6
  name: Api Security Host Info In Config Example
  slug: api-security-host-info-in-config-example
- key_count: 14
  name: Api Security Hostname Coverage Match Target Example
  slug: api-security-hostname-coverage-match-target-example
- key_count: 1
  name: Api Security Hostname Coverage Match Target Get 200 Example
  slug: api-security-hostname-coverage-match-target-get-200-example
- key_count: 1
  name: Api Security Hostname Coverage Overlapping Get 200 Example
  slug: api-security-hostname-coverage-overlapping-get-200-example
- key_count: 6
  name: Api Security Hostname Object Example
  slug: api-security-hostname-object-example
- key_count: 2
  name: Api Security Hostnames Example
  slug: api-security-hostnames-example
- key_count: 2
  name: Api Security Logging Header Setting Example
  slug: api-security-logging-header-setting-example
- key_count: 3
  name: Api Security Logging Option Example
  slug: api-security-logging-option-example
- key_count: 1
  name: Api Security Malware Policies Content Types Example
  slug: api-security-malware-policies-content-types-example
- key_count: 1
  name: Api Security Malware Policies Example
  slug: api-security-malware-policies-example
- key_count: 9
  name: Api Security Malware Policy Example
  slug: api-security-malware-policy-example
- key_count: 16
  name: Api Security Match Target Example
  slug: api-security-match-target-example
- key_count: 1
  name: Api Security Match Targets Example
  slug: api-security-match-targets-example
- key_count: 2
  name: Api Security Match Targets Sequence Example
  slug: api-security-match-targets-sequence-example
- key_count: 6
  name: Api Security Overlap Config Example
  slug: api-security-overlap-config-example
- key_count: 1
  name: Api Security Pii Learning Example
  slug: api-security-pii-learning-example
- key_count: 3
  name: Api Security Pragma Header Example
  slug: api-security-pragma-header-example
- key_count: 4
  name: Api Security Prefetch Request Get 200 Example
  slug: api-security-prefetch-request-get-200-example
- key_count: 4
  name: Api Security Prefetch Request Put 200 Example
  slug: api-security-prefetch-request-put-200-example
- key_count: 4
  name: Api Security Prefetch Request Put Example
  slug: api-security-prefetch-request-put-example
- key_count: 6
  name: Api Security Problem Details Example
  slug: api-security-problem-details-example
- key_count: 1
  name: Api Security Rate Policies Example
  slug: api-security-rate-policies-example
- key_count: 1
  name: Api Security Rate Policy Evaluation Put Example
  slug: api-security-rate-policy-evaluation-put-example
- key_count: 28
  name: Api Security Rate Policy Example
  slug: api-security-rate-policy-example
- key_count: 9
  name: Api Security Reputation Profile Example
  slug: api-security-reputation-profile-example
- key_count: 1
  name: Api Security Reputation Profiles Example
  slug: api-security-reputation-profiles-example
- key_count: 1
  name: Api Security Request Body Example
  slug: api-security-request-body-example
- key_count: 7
  name: Api Security Request Header Condition 2 Example
  slug: api-security-request-header-condition-2-example
- key_count: 7
  name: Api Security Security Controls Example
  slug: api-security-security-controls-example
- key_count: 6
  name: Api Security Siem Settings Example
  slug: api-security-siem-settings-example
- key_count: 2
  name: Api Security Siem Version Example
  slug: api-security-siem-version-example
- key_count: 1
  name: Api Security Siem Versions Example
  slug: api-security-siem-versions-example
- key_count: 3
  name: Api Security Tls Fingerprint Condition Example
  slug: api-security-tls-fingerprint-condition-example
- key_count: 4
  name: Api Security Url Protection Bypass Client List Condition Example
  slug: api-security-url-protection-bypass-client-list-condition-example
- key_count: 7
  name: Api Security Url Protection Bypass Request Header Condition Example
  slug: api-security-url-protection-bypass-request-header-condition-example
- key_count: 1
  name: Api Security Url Protection Category Example
  slug: api-security-url-protection-category-example
- key_count: 3
  name: Api Security Url Protection Client List Category Example
  slug: api-security-url-protection-client-list-category-example
- key_count: 1
  name: Api Security Url Protection Policies Example
  slug: api-security-url-protection-policies-example
- key_count: 18
  name: Api Security Url Protection Policy Example
  slug: api-security-url-protection-policy-example
- key_count: 2
  name: Api Security Url Protection Policy Hostpath Example
  slug: api-security-url-protection-policy-hostpath-example
- key_count: 5
  name: Api Security Validation Example
  slug: api-security-validation-example
- key_count: 3
  name: Api Security Validations Example
  slug: api-security-validations-example
- key_count: 1
  name: Api Security Version Notes Get 200 Example
  slug: api-security-version-notes-get-200-example
- key_count: 1
  name: Api Security Version Notes Put 200 Example
  slug: api-security-version-notes-put-200-example
- key_count: 1
  name: Api Security Version Notes Put Example
  slug: api-security-version-notes-put-example
- key_count: 9
  name: Api Security Waf Config Version Example
  slug: api-security-waf-config-version-example
- key_count: 11
  name: Api Security Waf Config Versions Example
  slug: api-security-waf-config-versions-example
features:
- description: Automatically discovers all APIs including shadow, zombie, GenAI, LLM, and MCP server APIs across cloud, on-premises, and hybrid environments.
  name: API Discovery
- description: Audits APIs for vulnerabilities and misconfigurations including the full OWASP API Top 10, generating posture findings from runtime incidents.
  name: Posture Management
- description: Uses contextual insights to detect and block API threats including business logic abuse, credential attacks, data scraping, and malicious bots in real time.
  name: Runtime Protection
- description: Runs 200+ dynamic security tests simulating OWASP API Top 10 attacks integrated into CI/CD pipelines without sacrificing development speed.
  name: CI/CD Security Testing
- description: Automatically scans GitHub repositories for OpenAPI specs and adds them to the API library for security analysis and posture assessment.
  name: GitHub Integration
- description: Direct integration with Akamai App and API Protector for blocking API threats detected at runtime.
  name: App and API Protector Integration
finops:
- name: Akamai Api Security Finops
  service_category: API
  slug: akamai-api-security-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akamai-api-security.png
integrations:
- description: Direct integration for blocking API threats detected by API Security
  name: Akamai App and API Protector
- description: Automatic OpenAPI spec discovery from GitHub repositories
  name: GitHub
- description: Integration with development pipelines for pre-production security testing
  name: CI/CD Pipelines
- description: Export security events to SIEM platforms for centralized monitoring
  name: SIEM
- description: Available on AWS Marketplace for cloud-native deployments
  name: AWS Marketplace
json_schemas:
- name: attack-payload-logging-get-200
  property_count: 3
  slug: api-security-attack-payload-logging-get-200
- name: attack-payload-logging-put-200
  property_count: 3
  slug: api-security-attack-payload-logging-put-200
- name: attack-payload-logging-put
  property_count: 3
  slug: api-security-attack-payload-logging-put
- name: attack-payload-logging
  property_count: 1
  slug: api-security-attack-payload-logging
- name: bypass-network-lists-get
  property_count: 1
  slug: api-security-bypass-network-lists-get
- name: bypass-network-lists-put
  property_count: 1
  slug: api-security-bypass-network-lists-put
- name: client-reputation-condition
  property_count: 5
  slug: api-security-client-reputation-condition
- name: config-clone-post
  property_count: 2
  slug: api-security-config-clone-post
- name: config-get
  property_count: 7
  slug: api-security-config-get
- name: config-post
  property_count: 6
  slug: api-security-config-post
- name: config-rename
  property_count: 2
  slug: api-security-config-rename
- name: configs-get
  property_count: 1
  slug: api-security-configs-get
- name: cookie-settings
  property_count: 2
  slug: api-security-cookie-settings
- name: custom-denies
  property_count: 1
  slug: api-security-custom-denies
- name: custom-deny
  property_count: 4
  slug: api-security-custom-deny
- name: custom-rule
  property_count: 16
  slug: api-security-custom-rule
- name: custom-rules
  property_count: 1
  slug: api-security-custom-rules
- name: effectiveTimePeriod
  property_count: 3
  slug: api-security-effective-time-period
- name: evasive-path-match-get-200
  property_count: 1
  slug: api-security-evasive-path-match-get-200
- name: evasive-path-match-put-200
  property_count: 1
  slug: api-security-evasive-path-match-put-200
- name: evasive-path-match-put
  property_count: 1
  slug: api-security-evasive-path-match-put
- name: header-logging-get-200
  property_count: 4
  slug: api-security-header-logging-get-200
- name: header-logging-put-200
  property_count: 4
  slug: api-security-header-logging-put-200
- name: header-logging-put
  property_count: 4
  slug: api-security-header-logging-put
- name: host-info-in-config
  property_count: 6
  slug: api-security-host-info-in-config
- name: hostname-coverage-match-target-get-200
  property_count: 1
  slug: api-security-hostname-coverage-match-target-get-200
- name: hostname-coverage-match-target
  property_count: 14
  slug: api-security-hostname-coverage-match-target
- name: hostname-coverage-overlapping-get-200
  property_count: 1
  slug: api-security-hostname-coverage-overlapping-get-200
- name: hostname-object
  property_count: 6
  slug: api-security-hostname-object
- name: hostnames
  property_count: 2
  slug: api-security-hostnames
- name: logging-header-setting
  property_count: 2
  slug: api-security-logging-header-setting
- name: logging-option
  property_count: 3
  slug: api-security-logging-option
- name: malware-policies-content-types
  property_count: 1
  slug: api-security-malware-policies-content-types
- name: malware-policies
  property_count: 1
  slug: api-security-malware-policies
- name: malware-policy
  property_count: 9
  slug: api-security-malware-policy
- name: match-target
  property_count: 16
  slug: api-security-match-target
- name: match-targets
  property_count: 1
  slug: api-security-match-targets
- name: match-targets-sequence
  property_count: 2
  slug: api-security-match-targets-sequence
- name: overlap-config
  property_count: 6
  slug: api-security-overlap-config
- name: pii-learning
  property_count: 1
  slug: api-security-pii-learning
- name: pragma-header
  property_count: 3
  slug: api-security-pragma-header
- name: prefetch-request-get-200
  property_count: 4
  slug: api-security-prefetch-request-get-200
- name: prefetch-request-put-200
  property_count: 4
  slug: api-security-prefetch-request-put-200
- name: prefetch-request-put
  property_count: 4
  slug: api-security-prefetch-request-put
- name: problem-details
  property_count: 6
  slug: api-security-problem-details
- name: rate-policies
  property_count: 1
  slug: api-security-rate-policies
- name: rate-policy-evaluation-put
  property_count: 1
  slug: api-security-rate-policy-evaluation-put
- name: rate-policy
  property_count: 28
  slug: api-security-rate-policy
- name: reputation-profile
  property_count: 9
  slug: api-security-reputation-profile
- name: reputation-profiles
  property_count: 1
  slug: api-security-reputation-profiles
- name: request-body
  property_count: 1
  slug: api-security-request-body
- name: request-header-condition-2
  property_count: 7
  slug: api-security-request-header-condition-2
- name: security-controls
  property_count: 7
  slug: api-security-security-controls
- name: siem-settings
  property_count: 6
  slug: api-security-siem-settings
- name: siem-version
  property_count: 2
  slug: api-security-siem-version
- name: siem-versions
  property_count: 1
  slug: api-security-siem-versions
- name: tls-fingerprint-condition
  property_count: 3
  slug: api-security-tls-fingerprint-condition
- name: url-protection-bypass-client-list-condition
  property_count: 4
  slug: api-security-url-protection-bypass-client-list-condition
- name: url-protection-bypass-request-header-condition
  property_count: 7
  slug: api-security-url-protection-bypass-request-header-condition
- name: url-protection-category
  property_count: 1
  slug: api-security-url-protection-category
- name: url-protection-client-list-category
  property_count: 3
  slug: api-security-url-protection-client-list-category
- name: url-protection-policies
  property_count: 1
  slug: api-security-url-protection-policies
- name: url-protection-policy-hostpath
  property_count: 2
  slug: api-security-url-protection-policy-hostpath
- name: url-protection-policy
  property_count: 18
  slug: api-security-url-protection-policy
- name: validation
  property_count: 5
  slug: api-security-validation
- name: validations
  property_count: 3
  slug: api-security-validations
- name: version-notes-get-200
  property_count: 1
  slug: api-security-version-notes-get-200
- name: version-notes-put-200
  property_count: 1
  slug: api-security-version-notes-put-200
- name: version-notes-put
  property_count: 1
  slug: api-security-version-notes-put
- name: waf-config-version
  property_count: 9
  slug: api-security-waf-config-version
- name: waf-config-versions
  property_count: 11
  slug: api-security-waf-config-versions
json_structures:
- name: Api Security Attack Payload Logging Get 200 Structure
  property_count: 3
  slug: api-security-attack-payload-logging-get-200-structure
- name: Api Security Attack Payload Logging Put 200 Structure
  property_count: 3
  slug: api-security-attack-payload-logging-put-200-structure
- name: Api Security Attack Payload Logging Put Structure
  property_count: 3
  slug: api-security-attack-payload-logging-put-structure
- name: Api Security Attack Payload Logging Structure
  property_count: 1
  slug: api-security-attack-payload-logging-structure
- name: Api Security Bypass Network Lists Get Structure
  property_count: 1
  slug: api-security-bypass-network-lists-get-structure
- name: Api Security Bypass Network Lists Put Structure
  property_count: 1
  slug: api-security-bypass-network-lists-put-structure
- name: Api Security Client Reputation Condition Structure
  property_count: 5
  slug: api-security-client-reputation-condition-structure
- name: Api Security Config Clone Post Structure
  property_count: 2
  slug: api-security-config-clone-post-structure
- name: Api Security Config Get Structure
  property_count: 7
  slug: api-security-config-get-structure
- name: Api Security Config Post Structure
  property_count: 6
  slug: api-security-config-post-structure
- name: Api Security Config Rename Structure
  property_count: 2
  slug: api-security-config-rename-structure
- name: Api Security Configs Get Structure
  property_count: 1
  slug: api-security-configs-get-structure
- name: Api Security Cookie Settings Structure
  property_count: 2
  slug: api-security-cookie-settings-structure
- name: Api Security Custom Denies Structure
  property_count: 1
  slug: api-security-custom-denies-structure
- name: Api Security Custom Deny Structure
  property_count: 4
  slug: api-security-custom-deny-structure
- name: Api Security Custom Rule Structure
  property_count: 16
  slug: api-security-custom-rule-structure
- name: Api Security Custom Rules Structure
  property_count: 1
  slug: api-security-custom-rules-structure
- name: Api Security Effective Time Period Structure
  property_count: 3
  slug: api-security-effective-time-period-structure
- name: Api Security Evasive Path Match Get 200 Structure
  property_count: 1
  slug: api-security-evasive-path-match-get-200-structure
- name: Api Security Evasive Path Match Put 200 Structure
  property_count: 1
  slug: api-security-evasive-path-match-put-200-structure
- name: Api Security Evasive Path Match Put Structure
  property_count: 1
  slug: api-security-evasive-path-match-put-structure
- name: Api Security Header Logging Get 200 Structure
  property_count: 4
  slug: api-security-header-logging-get-200-structure
- name: Api Security Header Logging Put 200 Structure
  property_count: 4
  slug: api-security-header-logging-put-200-structure
- name: Api Security Header Logging Put Structure
  property_count: 4
  slug: api-security-header-logging-put-structure
- name: Api Security Host Info In Config Structure
  property_count: 6
  slug: api-security-host-info-in-config-structure
- name: Api Security Hostname Coverage Match Target Get 200 Structure
  property_count: 1
  slug: api-security-hostname-coverage-match-target-get-200-structure
- name: Api Security Hostname Coverage Match Target Structure
  property_count: 14
  slug: api-security-hostname-coverage-match-target-structure
- name: Api Security Hostname Coverage Overlapping Get 200 Structure
  property_count: 1
  slug: api-security-hostname-coverage-overlapping-get-200-structure
- name: Api Security Hostname Object Structure
  property_count: 6
  slug: api-security-hostname-object-structure
- name: Api Security Hostnames Structure
  property_count: 2
  slug: api-security-hostnames-structure
- name: Api Security Logging Header Setting Structure
  property_count: 2
  slug: api-security-logging-header-setting-structure
- name: Api Security Logging Option Structure
  property_count: 3
  slug: api-security-logging-option-structure
- name: Api Security Malware Policies Content Types Structure
  property_count: 1
  slug: api-security-malware-policies-content-types-structure
- name: Api Security Malware Policies Structure
  property_count: 1
  slug: api-security-malware-policies-structure
- name: Api Security Malware Policy Structure
  property_count: 9
  slug: api-security-malware-policy-structure
- name: Api Security Match Target Structure
  property_count: 16
  slug: api-security-match-target-structure
- name: Api Security Match Targets Sequence Structure
  property_count: 2
  slug: api-security-match-targets-sequence-structure
- name: Api Security Match Targets Structure
  property_count: 1
  slug: api-security-match-targets-structure
- name: Api Security Overlap Config Structure
  property_count: 6
  slug: api-security-overlap-config-structure
- name: Api Security Pii Learning Structure
  property_count: 1
  slug: api-security-pii-learning-structure
- name: Api Security Pragma Header Structure
  property_count: 3
  slug: api-security-pragma-header-structure
- name: Api Security Prefetch Request Get 200 Structure
  property_count: 4
  slug: api-security-prefetch-request-get-200-structure
- name: Api Security Prefetch Request Put 200 Structure
  property_count: 4
  slug: api-security-prefetch-request-put-200-structure
- name: Api Security Prefetch Request Put Structure
  property_count: 4
  slug: api-security-prefetch-request-put-structure
- name: Api Security Problem Details Structure
  property_count: 6
  slug: api-security-problem-details-structure
- name: Api Security Rate Policies Structure
  property_count: 1
  slug: api-security-rate-policies-structure
- name: Api Security Rate Policy Evaluation Put Structure
  property_count: 1
  slug: api-security-rate-policy-evaluation-put-structure
- name: Api Security Rate Policy Structure
  property_count: 28
  slug: api-security-rate-policy-structure
- name: Api Security Reputation Profile Structure
  property_count: 9
  slug: api-security-reputation-profile-structure
- name: Api Security Reputation Profiles Structure
  property_count: 1
  slug: api-security-reputation-profiles-structure
- name: Api Security Request Body Structure
  property_count: 1
  slug: api-security-request-body-structure
- name: Api Security Request Header Condition 2 Structure
  property_count: 7
  slug: api-security-request-header-condition-2-structure
- name: Api Security Security Controls Structure
  property_count: 7
  slug: api-security-security-controls-structure
- name: Api Security Siem Settings Structure
  property_count: 6
  slug: api-security-siem-settings-structure
- name: Api Security Siem Version Structure
  property_count: 2
  slug: api-security-siem-version-structure
- name: Api Security Siem Versions Structure
  property_count: 1
  slug: api-security-siem-versions-structure
- name: Api Security Tls Fingerprint Condition Structure
  property_count: 3
  slug: api-security-tls-fingerprint-condition-structure
- name: Api Security Url Protection Bypass Client List Condition Structure
  property_count: 4
  slug: api-security-url-protection-bypass-client-list-condition-structure
- name: Api Security Url Protection Bypass Request Header Condition Structure
  property_count: 7
  slug: api-security-url-protection-bypass-request-header-condition-structure
- name: Api Security Url Protection Category Structure
  property_count: 1
  slug: api-security-url-protection-category-structure
- name: Api Security Url Protection Client List Category Structure
  property_count: 3
  slug: api-security-url-protection-client-list-category-structure
- name: Api Security Url Protection Policies Structure
  property_count: 1
  slug: api-security-url-protection-policies-structure
- name: Api Security Url Protection Policy Hostpath Structure
  property_count: 2
  slug: api-security-url-protection-policy-hostpath-structure
- name: Api Security Url Protection Policy Structure
  property_count: 18
  slug: api-security-url-protection-policy-structure
- name: Api Security Validation Structure
  property_count: 5
  slug: api-security-validation-structure
- name: Api Security Validations Structure
  property_count: 3
  slug: api-security-validations-structure
- name: Api Security Version Notes Get 200 Structure
  property_count: 1
  slug: api-security-version-notes-get-200-structure
- name: Api Security Version Notes Put 200 Structure
  property_count: 1
  slug: api-security-version-notes-put-200-structure
- name: Api Security Version Notes Put Structure
  property_count: 1
  slug: api-security-version-notes-put-structure
- name: Api Security Waf Config Version Structure
  property_count: 9
  slug: api-security-waf-config-version-structure
- name: Api Security Waf Config Versions Structure
  property_count: 11
  slug: api-security-waf-config-versions-structure
jsonld:
- class_count: 71
  name: Akamai Api Security Context
  property_count: 180
  slug: akamai-api-security-context
layout: provider
modified: '2026-05-19'
name: Akamai API Security
nav: Providers
network: true
overview: 'Akamai API Security publishes 64 APIs on the [APIs.io](https://apis.io/) network, including Activation history API, Activation status API, Activations API, and 61 more. Tagged areas include API Discovery, API Security, Cloud Security, Posture Management, and Runtime Protection.


  The Akamai API Security catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Akamai API Security''s developer surface includes documentation, engineering blog, pricing, support, signup flow, and 10 more developer resources.'
plans:
- name: Akamai Api Security Plans Pricing
  plan_count: 3
  slug: akamai-api-security-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Akamai Api Security Rate Limits
  slug: akamai-api-security-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Akamai API Security API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: akamai-api-security-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Akamai API Security API Rules
  rule_count: 28
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 15
  slug: akamai-api-security-spectral-rules
score:
  band: thin
  composite: 36.0
  delta: -7.1
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 25.0
    contract_quality: 58.7
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 43.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 64
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/akamai-api-security/refs/heads/main/screenshots/akamai-api-security-2026-06-20T171447.png
security:
- kind: domain-security
  name: Akamai Api Security Domain Security
  slug: akamai-api-security-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: akamai-api-security
tags:
- API Discovery
- API Security
- Cloud Security
- Posture Management
- Runtime Protection
- Threat Protection
use_cases:
- description: Security teams automatically discover undocumented and shadow APIs across their environment to eliminate blind spots.
  name: Shadow API Discovery
- description: Security engineers assess API posture against OWASP API Top 10 and compliance frameworks to prioritize remediation.
  name: API Vulnerability Assessment
- description: SOC analysts detect and respond to API attacks, data leakage, and suspicious behavior in real time.
  name: Real-Time Threat Detection
- description: Development teams integrate API security testing into CI/CD pipelines to find and fix vulnerabilities before production.
  name: Pre-Production API Testing
- description: Compliance teams assess API security posture against industry frameworks and generate audit-ready reports.
  name: Compliance Reporting
website: https://www.akamai.com/products/api-security
---
