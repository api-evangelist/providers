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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.6
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 48
  human_in_the_loop: 2
  name: Amazon Guardduty Agentic Access
  operation_count: 67
  slug: amazon-guardduty-agentic-access
  summary_line: 67 operations · 48 acting · 2 human-in-the-loop
api_count: 4
apis:
- description: The Admin API from Amazon GuardDuty — 3 operation(s) for admin.
  name: Amazon GuardDuty Admin API
  slug: amazon-guardduty-admin-api
- description: The Detector API from Amazon GuardDuty — 37 operation(s) for detector.
  name: Amazon GuardDuty Detector API
  slug: amazon-guardduty-detector-api
- description: The Invitation API from Amazon GuardDuty — 4 operation(s) for invitation.
  name: Amazon GuardDuty Invitation API
  slug: amazon-guardduty-invitation-api
- description: The Tags API from Amazon GuardDuty — 2 operation(s) for tags.
  name: Amazon GuardDuty Tags API
  slug: amazon-guardduty-tags-api
artifact_total: 1222
collections:
- collection_type: postman
  name: Amazon GuardDuty Admin API
  slug: postman-amazon-guardduty-admin-api
- collection_type: postman
  name: Amazon GuardDuty Admin Detector API
  slug: postman-amazon-guardduty-detector-api
- collection_type: postman
  name: Amazon GuardDuty Admin Invitation API
  slug: postman-amazon-guardduty-invitation-api
- collection_type: postman
  name: Amazon GuardDuty Admin Tags API
  slug: postman-amazon-guardduty-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon GuardDuty Admin API
  slug: open-amazon-guardduty-admin-api
- collection_type: open
  name: Amazon GuardDuty Admin Detector API
  slug: open-amazon-guardduty-detector-api
- collection_type: open
  name: Amazon GuardDuty Admin Invitation API
  slug: open-amazon-guardduty-invitation-api
- collection_type: open
  name: Amazon GuardDuty Admin Tags API
  slug: open-amazon-guardduty-tags-api
- collection_type: open
  name: Amazon GuardDuty
  slug: open-amazon-guardduty
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-guardduty/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-guardduty-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-guardduty-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-guardduty-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-guardduty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-guardduty-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/guardduty/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/guardduty/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/security/tag/amazon-guardduty/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/guardduty/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-guardduty-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-guardduty-vocabulary.yaml
created: '2024-01-15'
description: Amazon GuardDuty is an intelligent threat detection service that continuously monitors your AWS accounts, workloads, and data for malicious activity. It uses machine learning, anomaly detection, and integrated threat intelligence to identify and prioritize potential threats to your AWS environment.
examples:
- key_count: 6
  name: Amazon Guardduty Example
  slug: amazon-guardduty-example
- key_count: 2
  name: Guardduty Accept Administrator Invitation Request Example
  slug: guardduty-accept-administrator-invitation-request-example
- key_count: 0
  name: Guardduty Accept Administrator Invitation Response Example
  slug: guardduty-accept-administrator-invitation-response-example
- key_count: 2
  name: Guardduty Accept Invitation Request Example
  slug: guardduty-accept-invitation-request-example
- key_count: 0
  name: Guardduty Accept Invitation Response Example
  slug: guardduty-accept-invitation-response-example
- key_count: 2
  name: Guardduty Access Control List Example
  slug: guardduty-access-control-list-example
- key_count: 4
  name: Guardduty Access Key Details Example
  slug: guardduty-access-key-details-example
- key_count: 2
  name: Guardduty Account Detail Example
  slug: guardduty-account-detail-example
- key_count: 3
  name: Guardduty Account Free Trial Info Example
  slug: guardduty-account-free-trial-info-example
- key_count: 1
  name: Guardduty Account Level Permissions Example
  slug: guardduty-account-level-permissions-example
- key_count: 6
  name: Guardduty Action Example
  slug: guardduty-action-example
- key_count: 2
  name: Guardduty Addon Details Example
  slug: guardduty-addon-details-example
- key_count: 2
  name: Guardduty Admin Account Example
  slug: guardduty-admin-account-example
- key_count: 4
  name: Guardduty Administrator Example
  slug: guardduty-administrator-example
- key_count: 0
  name: Guardduty Affected Resources Example
  slug: guardduty-affected-resources-example
- key_count: 1
  name: Guardduty Archive Findings Request Example
  slug: guardduty-archive-findings-request-example
- key_count: 0
  name: Guardduty Archive Findings Response Example
  slug: guardduty-archive-findings-response-example
- key_count: 6
  name: Guardduty Aws Api Call Action Example
  slug: guardduty-aws-api-call-action-example
- key_count: 4
  name: Guardduty Block Public Access Example
  slug: guardduty-block-public-access-example
- key_count: 3
  name: Guardduty Bucket Level Permissions Example
  slug: guardduty-bucket-level-permissions-example
- key_count: 2
  name: Guardduty Bucket Policy Example
  slug: guardduty-bucket-policy-example
- key_count: 1
  name: Guardduty City Example
  slug: guardduty-city-example
- key_count: 1
  name: Guardduty Cloud Trail Configuration Result Example
  slug: guardduty-cloud-trail-configuration-result-example
- key_count: 6
  name: Guardduty Condition Example
  slug: guardduty-condition-example
- key_count: 6
  name: Guardduty Container Example
  slug: guardduty-container-example
- key_count: 0
  name: Guardduty Count By Coverage Status Example
  slug: guardduty-count-by-coverage-status-example
- key_count: 0
  name: Guardduty Count By Resource Type Example
  slug: guardduty-count-by-resource-type-example
- key_count: 0
  name: Guardduty Count By Severity Example
  slug: guardduty-count-by-severity-example
- key_count: 2
  name: Guardduty Country Example
  slug: guardduty-country-example
- key_count: 4
  name: Guardduty Coverage Eks Cluster Details Example
  slug: guardduty-coverage-eks-cluster-details-example
- key_count: 2
  name: Guardduty Coverage Filter Condition Example
  slug: guardduty-coverage-filter-condition-example
- key_count: 1
  name: Guardduty Coverage Filter Criteria Example
  slug: guardduty-coverage-filter-criteria-example
- key_count: 2
  name: Guardduty Coverage Filter Criterion Example
  slug: guardduty-coverage-filter-criterion-example
- key_count: 2
  name: Guardduty Coverage Resource Details Example
  slug: guardduty-coverage-resource-details-example
- key_count: 6
  name: Guardduty Coverage Resource Example
  slug: guardduty-coverage-resource-example
- key_count: 2
  name: Guardduty Coverage Sort Criteria Example
  slug: guardduty-coverage-sort-criteria-example
- key_count: 2
  name: Guardduty Coverage Statistics Example
  slug: guardduty-coverage-statistics-example
- key_count: 6
  name: Guardduty Create Detector Request Example
  slug: guardduty-create-detector-request-example
- key_count: 2
  name: Guardduty Create Detector Response Example
  slug: guardduty-create-detector-response-example
- key_count: 6
  name: Guardduty Create Filter Request Example
  slug: guardduty-create-filter-request-example
- key_count: 1
  name: Guardduty Create Filter Response Example
  slug: guardduty-create-filter-response-example
- key_count: 6
  name: Guardduty Create Ip Set Request Example
  slug: guardduty-create-ip-set-request-example
- key_count: 1
  name: Guardduty Create Ip Set Response Example
  slug: guardduty-create-ip-set-response-example
- key_count: 1
  name: Guardduty Create Members Request Example
  slug: guardduty-create-members-request-example
- key_count: 1
  name: Guardduty Create Members Response Example
  slug: guardduty-create-members-response-example
- key_count: 3
  name: Guardduty Create Publishing Destination Request Example
  slug: guardduty-create-publishing-destination-request-example
- key_count: 1
  name: Guardduty Create Publishing Destination Response Example
  slug: guardduty-create-publishing-destination-response-example
- key_count: 1
  name: Guardduty Create Sample Findings Request Example
  slug: guardduty-create-sample-findings-request-example
- key_count: 0
  name: Guardduty Create Sample Findings Response Example
  slug: guardduty-create-sample-findings-response-example
- key_count: 6
  name: Guardduty Create Threat Intel Set Request Example
  slug: guardduty-create-threat-intel-set-request-example
- key_count: 1
  name: Guardduty Create Threat Intel Set Response Example
  slug: guardduty-create-threat-intel-set-response-example
- key_count: 0
  name: Guardduty Criterion Example
  slug: guardduty-criterion-example
- key_count: 3
  name: Guardduty Data Source Configurations Example
  slug: guardduty-data-source-configurations-example
- key_count: 6
  name: Guardduty Data Source Configurations Result Example
  slug: guardduty-data-source-configurations-result-example
- key_count: 1
  name: Guardduty Data Source Free Trial Example
  slug: guardduty-data-source-free-trial-example
- key_count: 6
  name: Guardduty Data Sources Free Trial Example
  slug: guardduty-data-sources-free-trial-example
- key_count: 1
  name: Guardduty Decline Invitations Request Example
  slug: guardduty-decline-invitations-request-example
- key_count: 1
  name: Guardduty Decline Invitations Response Example
  slug: guardduty-decline-invitations-response-example
- key_count: 2
  name: Guardduty Default Server Side Encryption Example
  slug: guardduty-default-server-side-encryption-example
- key_count: 0
  name: Guardduty Delete Detector Request Example
  slug: guardduty-delete-detector-request-example
- key_count: 0
  name: Guardduty Delete Detector Response Example
  slug: guardduty-delete-detector-response-example
- key_count: 0
  name: Guardduty Delete Filter Request Example
  slug: guardduty-delete-filter-request-example
- key_count: 0
  name: Guardduty Delete Filter Response Example
  slug: guardduty-delete-filter-response-example
- key_count: 1
  name: Guardduty Delete Invitations Request Example
  slug: guardduty-delete-invitations-request-example
- key_count: 1
  name: Guardduty Delete Invitations Response Example
  slug: guardduty-delete-invitations-response-example
- key_count: 0
  name: Guardduty Delete Ip Set Request Example
  slug: guardduty-delete-ip-set-request-example
- key_count: 0
  name: Guardduty Delete Ip Set Response Example
  slug: guardduty-delete-ip-set-response-example
- key_count: 1
  name: Guardduty Delete Members Request Example
  slug: guardduty-delete-members-request-example
- key_count: 1
  name: Guardduty Delete Members Response Example
  slug: guardduty-delete-members-response-example
- key_count: 0
  name: Guardduty Delete Publishing Destination Request Example
  slug: guardduty-delete-publishing-destination-request-example
- key_count: 0
  name: Guardduty Delete Publishing Destination Response Example
  slug: guardduty-delete-publishing-destination-response-example
- key_count: 0
  name: Guardduty Delete Threat Intel Set Request Example
  slug: guardduty-delete-threat-intel-set-request-example
- key_count: 0
  name: Guardduty Delete Threat Intel Set Response Example
  slug: guardduty-delete-threat-intel-set-response-example
- key_count: 4
  name: Guardduty Describe Malware Scans Request Example
  slug: guardduty-describe-malware-scans-request-example
- key_count: 2
  name: Guardduty Describe Malware Scans Response Example
  slug: guardduty-describe-malware-scans-response-example
- key_count: 0
  name: Guardduty Describe Organization Configuration Request Example
  slug: guardduty-describe-organization-configuration-request-example
- key_count: 6
  name: Guardduty Describe Organization Configuration Response Example
  slug: guardduty-describe-organization-configuration-response-example
- key_count: 0
  name: Guardduty Describe Publishing Destination Request Example
  slug: guardduty-describe-publishing-destination-request-example
- key_count: 5
  name: Guardduty Describe Publishing Destination Response Example
  slug: guardduty-describe-publishing-destination-response-example
- key_count: 3
  name: Guardduty Destination Example
  slug: guardduty-destination-example
- key_count: 2
  name: Guardduty Destination Properties Example
  slug: guardduty-destination-properties-example
- key_count: 2
  name: Guardduty Detector Additional Configuration Example
  slug: guardduty-detector-additional-configuration-example
- key_count: 3
  name: Guardduty Detector Additional Configuration Result Example
  slug: guardduty-detector-additional-configuration-result-example
- key_count: 3
  name: Guardduty Detector Feature Configuration Example
  slug: guardduty-detector-feature-configuration-example
- key_count: 4
  name: Guardduty Detector Feature Configuration Result Example
  slug: guardduty-detector-feature-configuration-result-example
- key_count: 1
  name: Guardduty Disable Organization Admin Account Request Example
  slug: guardduty-disable-organization-admin-account-request-example
- key_count: 0
  name: Guardduty Disable Organization Admin Account Response Example
  slug: guardduty-disable-organization-admin-account-response-example
- key_count: 0
  name: Guardduty Disassociate From Administrator Account Request Example
  slug: guardduty-disassociate-from-administrator-account-request-example
- key_count: 0
  name: Guardduty Disassociate From Administrator Account Response Example
  slug: guardduty-disassociate-from-administrator-account-response-example
- key_count: 0
  name: Guardduty Disassociate From Master Account Request Example
  slug: guardduty-disassociate-from-master-account-request-example
- key_count: 0
  name: Guardduty Disassociate From Master Account Response Example
  slug: guardduty-disassociate-from-master-account-response-example
- key_count: 1
  name: Guardduty Disassociate Members Request Example
  slug: guardduty-disassociate-members-request-example
- key_count: 1
  name: Guardduty Disassociate Members Response Example
  slug: guardduty-disassociate-members-response-example
- key_count: 1
  name: Guardduty Dns Logs Configuration Result Example
  slug: guardduty-dns-logs-configuration-result-example
- key_count: 3
  name: Guardduty Dns Request Action Example
  slug: guardduty-dns-request-action-example
- key_count: 1
  name: Guardduty Domain Details Example
  slug: guardduty-domain-details-example
- key_count: 2
  name: Guardduty Ebs Volume Details Example
  slug: guardduty-ebs-volume-details-example
- key_count: 6
  name: Guardduty Ebs Volume Scan Details Example
  slug: guardduty-ebs-volume-scan-details-example
- key_count: 2
  name: Guardduty Ebs Volumes Result Example
  slug: guardduty-ebs-volumes-result-example
- key_count: 6
  name: Guardduty Ecs Cluster Details Example
  slug: guardduty-ecs-cluster-details-example
- key_count: 6
  name: Guardduty Ecs Task Details Example
  slug: guardduty-ecs-task-details-example
- key_count: 6
  name: Guardduty Eks Cluster Details Example
  slug: guardduty-eks-cluster-details-example
- key_count: 1
  name: Guardduty Enable Organization Admin Account Request Example
  slug: guardduty-enable-organization-admin-account-request-example
- key_count: 0
  name: Guardduty Enable Organization Admin Account Response Example
  slug: guardduty-enable-organization-admin-account-response-example
- key_count: 1
  name: Guardduty Evidence Example
  slug: guardduty-evidence-example
- key_count: 3
  name: Guardduty Filter Condition Example
  slug: guardduty-filter-condition-example
- key_count: 1
  name: Guardduty Filter Criteria Example
  slug: guardduty-filter-criteria-example
- key_count: 2
  name: Guardduty Filter Criterion Example
  slug: guardduty-filter-criterion-example
- key_count: 1
  name: Guardduty Finding Criteria Example
  slug: guardduty-finding-criteria-example
- key_count: 6
  name: Guardduty Finding Example
  slug: guardduty-finding-example
- key_count: 1
  name: Guardduty Finding Statistics Example
  slug: guardduty-finding-statistics-example
- key_count: 1
  name: Guardduty Flow Logs Configuration Result Example
  slug: guardduty-flow-logs-configuration-result-example
- key_count: 2
  name: Guardduty Free Trial Feature Configuration Result Example
  slug: guardduty-free-trial-feature-configuration-result-example
- key_count: 2
  name: Guardduty Geo Location Example
  slug: guardduty-geo-location-example
- key_count: 0
  name: Guardduty Get Administrator Account Request Example
  slug: guardduty-get-administrator-account-request-example
- key_count: 1
  name: Guardduty Get Administrator Account Response Example
  slug: guardduty-get-administrator-account-response-example
- key_count: 2
  name: Guardduty Get Coverage Statistics Request Example
  slug: guardduty-get-coverage-statistics-request-example
- key_count: 1
  name: Guardduty Get Coverage Statistics Response Example
  slug: guardduty-get-coverage-statistics-response-example
- key_count: 0
  name: Guardduty Get Detector Request Example
  slug: guardduty-get-detector-request-example
- key_count: 6
  name: Guardduty Get Detector Response Example
  slug: guardduty-get-detector-response-example
- key_count: 0
  name: Guardduty Get Filter Request Example
  slug: guardduty-get-filter-request-example
- key_count: 6
  name: Guardduty Get Filter Response Example
  slug: guardduty-get-filter-response-example
- key_count: 2
  name: Guardduty Get Findings Request Example
  slug: guardduty-get-findings-request-example
- key_count: 1
  name: Guardduty Get Findings Response Example
  slug: guardduty-get-findings-response-example
- key_count: 2
  name: Guardduty Get Findings Statistics Request Example
  slug: guardduty-get-findings-statistics-request-example
- key_count: 1
  name: Guardduty Get Findings Statistics Response Example
  slug: guardduty-get-findings-statistics-response-example
- key_count: 0
  name: Guardduty Get Invitations Count Request Example
  slug: guardduty-get-invitations-count-request-example
- key_count: 1
  name: Guardduty Get Invitations Count Response Example
  slug: guardduty-get-invitations-count-response-example
- key_count: 0
  name: Guardduty Get Ip Set Request Example
  slug: guardduty-get-ip-set-request-example
- key_count: 5
  name: Guardduty Get Ip Set Response Example
  slug: guardduty-get-ip-set-response-example
- key_count: 0
  name: Guardduty Get Malware Scan Settings Request Example
  slug: guardduty-get-malware-scan-settings-request-example
- key_count: 2
  name: Guardduty Get Malware Scan Settings Response Example
  slug: guardduty-get-malware-scan-settings-response-example
- key_count: 0
  name: Guardduty Get Master Account Request Example
  slug: guardduty-get-master-account-request-example
- key_count: 1
  name: Guardduty Get Master Account Response Example
  slug: guardduty-get-master-account-response-example
- key_count: 1
  name: Guardduty Get Member Detectors Request Example
  slug: guardduty-get-member-detectors-request-example
- key_count: 2
  name: Guardduty Get Member Detectors Response Example
  slug: guardduty-get-member-detectors-response-example
- key_count: 1
  name: Guardduty Get Members Request Example
  slug: guardduty-get-members-request-example
- key_count: 2
  name: Guardduty Get Members Response Example
  slug: guardduty-get-members-response-example
- key_count: 1
  name: Guardduty Get Remaining Free Trial Days Request Example
  slug: guardduty-get-remaining-free-trial-days-request-example
- key_count: 2
  name: Guardduty Get Remaining Free Trial Days Response Example
  slug: guardduty-get-remaining-free-trial-days-response-example
- key_count: 0
  name: Guardduty Get Threat Intel Set Request Example
  slug: guardduty-get-threat-intel-set-request-example
- key_count: 5
  name: Guardduty Get Threat Intel Set Response Example
  slug: guardduty-get-threat-intel-set-response-example
- key_count: 5
  name: Guardduty Get Usage Statistics Request Example
  slug: guardduty-get-usage-statistics-request-example
- key_count: 2
  name: Guardduty Get Usage Statistics Response Example
  slug: guardduty-get-usage-statistics-response-example
- key_count: 3
  name: Guardduty Highest Severity Threat Details Example
  slug: guardduty-highest-severity-threat-details-example
- key_count: 1
  name: Guardduty Host Path Example
  slug: guardduty-host-path-example
- key_count: 2
  name: Guardduty Iam Instance Profile Example
  slug: guardduty-iam-instance-profile-example
- key_count: 6
  name: Guardduty Instance Details Example
  slug: guardduty-instance-details-example
- key_count: 4
  name: Guardduty Invitation Example
  slug: guardduty-invitation-example
- key_count: 3
  name: Guardduty Invite Members Request Example
  slug: guardduty-invite-members-request-example
- key_count: 1
  name: Guardduty Invite Members Response Example
  slug: guardduty-invite-members-response-example
- key_count: 6
  name: Guardduty Kubernetes Api Call Action Example
  slug: guardduty-kubernetes-api-call-action-example
- key_count: 1
  name: Guardduty Kubernetes Audit Logs Configuration Example
  slug: guardduty-kubernetes-audit-logs-configuration-example
- key_count: 1
  name: Guardduty Kubernetes Audit Logs Configuration Result Example
  slug: guardduty-kubernetes-audit-logs-configuration-result-example
- key_count: 1
  name: Guardduty Kubernetes Configuration Example
  slug: guardduty-kubernetes-configuration-example
- key_count: 1
  name: Guardduty Kubernetes Configuration Result Example
  slug: guardduty-kubernetes-configuration-result-example
- key_count: 1
  name: Guardduty Kubernetes Data Source Free Trial Example
  slug: guardduty-kubernetes-data-source-free-trial-example
- key_count: 2
  name: Guardduty Kubernetes Details Example
  slug: guardduty-kubernetes-details-example
- key_count: 3
  name: Guardduty Kubernetes User Details Example
  slug: guardduty-kubernetes-user-details-example
- key_count: 6
  name: Guardduty Kubernetes Workload Details Example
  slug: guardduty-kubernetes-workload-details-example
- key_count: 6
  name: Guardduty Lambda Details Example
  slug: guardduty-lambda-details-example
- key_count: 6
  name: Guardduty Lineage Object Example
  slug: guardduty-lineage-object-example
- key_count: 4
  name: Guardduty List Coverage Request Example
  slug: guardduty-list-coverage-request-example
- key_count: 2
  name: Guardduty List Coverage Response Example
  slug: guardduty-list-coverage-response-example
- key_count: 0
  name: Guardduty List Detectors Request Example
  slug: guardduty-list-detectors-request-example
- key_count: 2
  name: Guardduty List Detectors Response Example
  slug: guardduty-list-detectors-response-example
- key_count: 0
  name: Guardduty List Filters Request Example
  slug: guardduty-list-filters-request-example
- key_count: 2
  name: Guardduty List Filters Response Example
  slug: guardduty-list-filters-response-example
- key_count: 4
  name: Guardduty List Findings Request Example
  slug: guardduty-list-findings-request-example
- key_count: 2
  name: Guardduty List Findings Response Example
  slug: guardduty-list-findings-response-example
- key_count: 0
  name: Guardduty List Invitations Request Example
  slug: guardduty-list-invitations-request-example
- key_count: 2
  name: Guardduty List Invitations Response Example
  slug: guardduty-list-invitations-response-example
- key_count: 0
  name: Guardduty List Ip Sets Request Example
  slug: guardduty-list-ip-sets-request-example
- key_count: 2
  name: Guardduty List Ip Sets Response Example
  slug: guardduty-list-ip-sets-response-example
- key_count: 0
  name: Guardduty List Members Request Example
  slug: guardduty-list-members-request-example
- key_count: 2
  name: Guardduty List Members Response Example
  slug: guardduty-list-members-response-example
- key_count: 0
  name: Guardduty List Organization Admin Accounts Request Example
  slug: guardduty-list-organization-admin-accounts-request-example
- key_count: 2
  name: Guardduty List Organization Admin Accounts Response Example
  slug: guardduty-list-organization-admin-accounts-response-example
- key_count: 0
  name: Guardduty List Publishing Destinations Request Example
  slug: guardduty-list-publishing-destinations-request-example
- key_count: 2
  name: Guardduty List Publishing Destinations Response Example
  slug: guardduty-list-publishing-destinations-response-example
- key_count: 0
  name: Guardduty List Tags For Resource Request Example
  slug: guardduty-list-tags-for-resource-request-example
- key_count: 1
  name: Guardduty List Tags For Resource Response Example
  slug: guardduty-list-tags-for-resource-response-example
- key_count: 0
  name: Guardduty List Threat Intel Sets Request Example
  slug: guardduty-list-threat-intel-sets-request-example
- key_count: 2
  name: Guardduty List Threat Intel Sets Response Example
  slug: guardduty-list-threat-intel-sets-response-example
- key_count: 1
  name: Guardduty Local Ip Details Example
  slug: guardduty-local-ip-details-example
- key_count: 2
  name: Guardduty Local Port Details Example
  slug: guardduty-local-port-details-example
- key_count: 4
  name: Guardduty Login Attribute Example
  slug: guardduty-login-attribute-example
- key_count: 1
  name: Guardduty Malware Protection Configuration Example
  slug: guardduty-malware-protection-configuration-example
- key_count: 2
  name: Guardduty Malware Protection Configuration Result Example
  slug: guardduty-malware-protection-configuration-result-example
- key_count: 1
  name: Guardduty Malware Protection Data Source Free Trial Example
  slug: guardduty-malware-protection-data-source-free-trial-example
- key_count: 4
  name: Guardduty Master Example
  slug: guardduty-master-example
- key_count: 2
  name: Guardduty Member Additional Configuration Example
  slug: guardduty-member-additional-configuration-example
- key_count: 3
  name: Guardduty Member Additional Configuration Result Example
  slug: guardduty-member-additional-configuration-result-example
- key_count: 3
  name: Guardduty Member Data Source Configuration Example
  slug: guardduty-member-data-source-configuration-example
- key_count: 6
  name: Guardduty Member Example
  slug: guardduty-member-example
- key_count: 3
  name: Guardduty Member Features Configuration Example
  slug: guardduty-member-features-configuration-example
- key_count: 4
  name: Guardduty Member Features Configuration Result Example
  slug: guardduty-member-features-configuration-result-example
- key_count: 6
  name: Guardduty Network Connection Action Example
  slug: guardduty-network-connection-action-example
- key_count: 6
  name: Guardduty Network Interface Example
  slug: guardduty-network-interface-example
- key_count: 2
  name: Guardduty Organization Additional Configuration Example
  slug: guardduty-organization-additional-configuration-example
- key_count: 2
  name: Guardduty Organization Additional Configuration Result Example
  slug: guardduty-organization-additional-configuration-result-example
- key_count: 3
  name: Guardduty Organization Data Source Configurations Example
  slug: guardduty-organization-data-source-configurations-example
- key_count: 3
  name: Guardduty Organization Data Source Configurations Result Example
  slug: guardduty-organization-data-source-configurations-result-example
- key_count: 1
  name: Guardduty Organization Ebs Volumes Example
  slug: guardduty-organization-ebs-volumes-example
- key_count: 1
  name: Guardduty Organization Ebs Volumes Result Example
  slug: guardduty-organization-ebs-volumes-result-example
- key_count: 4
  name: Guardduty Organization Example
  slug: guardduty-organization-example
- key_count: 3
  name: Guardduty Organization Feature Configuration Example
  slug: guardduty-organization-feature-configuration-example
- key_count: 3
  name: Guardduty Organization Feature Configuration Result Example
  slug: guardduty-organization-feature-configuration-result-example
- key_count: 1
  name: Guardduty Organization Kubernetes Audit Logs Configuration Example
  slug: guardduty-organization-kubernetes-audit-logs-configuration-example
- key_count: 1
  name: Guardduty Organization Kubernetes Audit Logs Configuration Result Example
  slug: guardduty-organization-kubernetes-audit-logs-configuration-result-example
- key_count: 1
  name: Guardduty Organization Kubernetes Configuration Example
  slug: guardduty-organization-kubernetes-configuration-example
- key_count: 1
  name: Guardduty Organization Kubernetes Configuration Result Example
  slug: guardduty-organization-kubernetes-configuration-result-example
- key_count: 1
  name: Guardduty Organization Malware Protection Configuration Example
  slug: guardduty-organization-malware-protection-configuration-example
- key_count: 1
  name: Guardduty Organization Malware Protection Configuration Result Example
  slug: guardduty-organization-malware-protection-configuration-result-example
- key_count: 1
  name: Guardduty Organization S3 Logs Configuration Example
  slug: guardduty-organization-s3-logs-configuration-example
- key_count: 1
  name: Guardduty Organization S3 Logs Configuration Result Example
  slug: guardduty-organization-s3-logs-configuration-result-example
- key_count: 1
  name: Guardduty Organization Scan Ec2 Instance With Findings Example
  slug: guardduty-organization-scan-ec2-instance-with-findings-example
- key_count: 1
  name: Guardduty Organization Scan Ec2 Instance With Findings Result Example
  slug: guardduty-organization-scan-ec2-instance-with-findings-result-example
- key_count: 1
  name: Guardduty Owner Example
  slug: guardduty-owner-example
- key_count: 2
  name: Guardduty Permission Configuration Example
  slug: guardduty-permission-configuration-example
- key_count: 2
  name: Guardduty Port Probe Action Example
  slug: guardduty-port-probe-action-example
- key_count: 3
  name: Guardduty Port Probe Detail Example
  slug: guardduty-port-probe-detail-example
- key_count: 2
  name: Guardduty Private Ip Address Details Example
  slug: guardduty-private-ip-address-details-example
- key_count: 6
  name: Guardduty Process Details Example
  slug: guardduty-process-details-example
- key_count: 2
  name: Guardduty Product Code Example
  slug: guardduty-product-code-example
- key_count: 2
  name: Guardduty Public Access Example
  slug: guardduty-public-access-example
- key_count: 6
  name: Guardduty Rds Db Instance Details Example
  slug: guardduty-rds-db-instance-details-example
- key_count: 5
  name: Guardduty Rds Db User Details Example
  slug: guardduty-rds-db-user-details-example
- key_count: 2
  name: Guardduty Rds Login Attempt Action Example
  slug: guardduty-rds-login-attempt-action-example
- key_count: 2
  name: Guardduty Remote Account Details Example
  slug: guardduty-remote-account-details-example
- key_count: 5
  name: Guardduty Remote Ip Details Example
  slug: guardduty-remote-ip-details-example
- key_count: 2
  name: Guardduty Remote Port Details Example
  slug: guardduty-remote-port-details-example
- key_count: 1
  name: Guardduty Resource Details Example
  slug: guardduty-resource-details-example
- key_count: 6
  name: Guardduty Resource Example
  slug: guardduty-resource-example
- key_count: 6
  name: Guardduty Runtime Context Example
  slug: guardduty-runtime-context-example
- key_count: 2
  name: Guardduty Runtime Details Example
  slug: guardduty-runtime-details-example
- key_count: 6
  name: Guardduty S3 Bucket Detail Example
  slug: guardduty-s3-bucket-detail-example
- key_count: 1
  name: Guardduty S3 Logs Configuration Example
  slug: guardduty-s3-logs-configuration-example
- key_count: 1
  name: Guardduty S3 Logs Configuration Result Example
  slug: guardduty-s3-logs-configuration-result-example
- key_count: 1
  name: Guardduty Scan Condition Example
  slug: guardduty-scan-condition-example
- key_count: 2
  name: Guardduty Scan Condition Pair Example
  slug: guardduty-scan-condition-pair-example
- key_count: 0
  name: Guardduty Scan Criterion Example
  slug: guardduty-scan-criterion-example
- key_count: 4
  name: Guardduty Scan Detections Example
  slug: guardduty-scan-detections-example
- key_count: 1
  name: Guardduty Scan Ec2 Instance With Findings Example
  slug: guardduty-scan-ec2-instance-with-findings-example
- key_count: 1
  name: Guardduty Scan Ec2 Instance With Findings Result Example
  slug: guardduty-scan-ec2-instance-with-findings-result-example
- key_count: 6
  name: Guardduty Scan Example
  slug: guardduty-scan-example
- key_count: 4
  name: Guardduty Scan File Path Example
  slug: guardduty-scan-file-path-example
- key_count: 2
  name: Guardduty Scan Resource Criteria Example
  slug: guardduty-scan-resource-criteria-example
- key_count: 1
  name: Guardduty Scan Result Details Example
  slug: guardduty-scan-result-details-example
- key_count: 4
  name: Guardduty Scan Threat Name Example
  slug: guardduty-scan-threat-name-example
- key_count: 3
  name: Guardduty Scanned Item Count Example
  slug: guardduty-scanned-item-count-example
- key_count: 1
  name: Guardduty Security Context Example
  slug: guardduty-security-context-example
- key_count: 2
  name: Guardduty Security Group Example
  slug: guardduty-security-group-example
- key_count: 2
  name: Guardduty Service Additional Info Example
  slug: guardduty-service-additional-info-example
- key_count: 6
  name: Guardduty Service Example
  slug: guardduty-service-example
- key_count: 2
  name: Guardduty Sort Criteria Example
  slug: guardduty-sort-criteria-example
- key_count: 1
  name: Guardduty Start Monitoring Members Request Example
  slug: guardduty-start-monitoring-members-request-example
- key_count: 1
  name: Guardduty Start Monitoring Members Response Example
  slug: guardduty-start-monitoring-members-response-example
- key_count: 1
  name: Guardduty Stop Monitoring Members Request Example
  slug: guardduty-stop-monitoring-members-request-example
- key_count: 1
  name: Guardduty Stop Monitoring Members Response Example
  slug: guardduty-stop-monitoring-members-response-example
- key_count: 2
  name: Guardduty Tag Example
  slug: guardduty-tag-example
- key_count: 0
  name: Guardduty Tag Map Example
  slug: guardduty-tag-map-example
- key_count: 1
  name: Guardduty Tag Resource Request Example
  slug: guardduty-tag-resource-request-example
- key_count: 0
  name: Guardduty Tag Resource Response Example
  slug: guardduty-tag-resource-response-example
- key_count: 4
  name: Guardduty Threat Detected By Name Example
  slug: guardduty-threat-detected-by-name-example
- key_count: 2
  name: Guardduty Threat Intelligence Detail Example
  slug: guardduty-threat-intelligence-detail-example
- key_count: 1
  name: Guardduty Threats Detected Item Count Example
  slug: guardduty-threats-detected-item-count-example
- key_count: 2
  name: Guardduty Total Example
  slug: guardduty-total-example
- key_count: 2
  name: Guardduty Trigger Details Example
  slug: guardduty-trigger-details-example
- key_count: 1
  name: Guardduty Unarchive Findings Request Example
  slug: guardduty-unarchive-findings-request-example
- key_count: 0
  name: Guardduty Unarchive Findings Response Example
  slug: guardduty-unarchive-findings-response-example
- key_count: 2
  name: Guardduty Unprocessed Account Example
  slug: guardduty-unprocessed-account-example
- key_count: 1
  name: Guardduty Unprocessed Data Sources Result Example
  slug: guardduty-unprocessed-data-sources-result-example
- key_count: 0
  name: Guardduty Untag Resource Request Example
  slug: guardduty-untag-resource-request-example
- key_count: 0
  name: Guardduty Untag Resource Response Example
  slug: guardduty-untag-resource-response-example
- key_count: 4
  name: Guardduty Update Detector Request Example
  slug: guardduty-update-detector-request-example
- key_count: 0
  name: Guardduty Update Detector Response Example
  slug: guardduty-update-detector-response-example
- key_count: 4
  name: Guardduty Update Filter Request Example
  slug: guardduty-update-filter-request-example
- key_count: 1
  name: Guardduty Update Filter Response Example
  slug: guardduty-update-filter-response-example
- key_count: 3
  name: Guardduty Update Findings Feedback Request Example
  slug: guardduty-update-findings-feedback-request-example
- key_count: 0
  name: Guardduty Update Findings Feedback Response Example
  slug: guardduty-update-findings-feedback-response-example
- key_count: 3
  name: Guardduty Update Ip Set Request Example
  slug: guardduty-update-ip-set-request-example
- key_count: 0
  name: Guardduty Update Ip Set Response Example
  slug: guardduty-update-ip-set-response-example
- key_count: 2
  name: Guardduty Update Malware Scan Settings Request Example
  slug: guardduty-update-malware-scan-settings-request-example
- key_count: 0
  name: Guardduty Update Malware Scan Settings Response Example
  slug: guardduty-update-malware-scan-settings-response-example
- key_count: 3
  name: Guardduty Update Member Detectors Request Example
  slug: guardduty-update-member-detectors-request-example
- key_count: 1
  name: Guardduty Update Member Detectors Response Example
  slug: guardduty-update-member-detectors-response-example
- key_count: 4
  name: Guardduty Update Organization Configuration Request Example
  slug: guardduty-update-organization-configuration-request-example
- key_count: 0
  name: Guardduty Update Organization Configuration Response Example
  slug: guardduty-update-organization-configuration-response-example
- key_count: 1
  name: Guardduty Update Publishing Destination Request Example
  slug: guardduty-update-publishing-destination-request-example
- key_count: 0
  name: Guardduty Update Publishing Destination Response Example
  slug: guardduty-update-publishing-destination-response-example
- key_count: 3
  name: Guardduty Update Threat Intel Set Request Example
  slug: guardduty-update-threat-intel-set-request-example
- key_count: 0
  name: Guardduty Update Threat Intel Set Response Example
  slug: guardduty-update-threat-intel-set-response-example
- key_count: 2
  name: Guardduty Usage Account Result Example
  slug: guardduty-usage-account-result-example
- key_count: 4
  name: Guardduty Usage Criteria Example
  slug: guardduty-usage-criteria-example
- key_count: 2
  name: Guardduty Usage Data Source Result Example
  slug: guardduty-usage-data-source-result-example
- key_count: 2
  name: Guardduty Usage Feature Result Example
  slug: guardduty-usage-feature-result-example
- key_count: 2
  name: Guardduty Usage Resource Result Example
  slug: guardduty-usage-resource-result-example
- key_count: 5
  name: Guardduty Usage Statistics Example
  slug: guardduty-usage-statistics-example
- key_count: 6
  name: Guardduty Volume Detail Example
  slug: guardduty-volume-detail-example
- key_count: 2
  name: Guardduty Volume Example
  slug: guardduty-volume-example
- key_count: 2
  name: Guardduty Volume Mount Example
  slug: guardduty-volume-mount-example
- key_count: 3
  name: Guardduty Vpc Config Example
  slug: guardduty-vpc-config-example
features:
- description: Uses ML and anomaly detection to identify threats without manual configuration or rule management.
  name: Intelligent Threat Detection
- description: Incorporates curated threat intelligence feeds from AWS, CrowdStrike, and Proofpoint for enhanced detection.
  name: Integrated Threat Intelligence
- description: Monitor all accounts in an AWS Organization from a central administrator account.
  name: Multi-Account Support
- description: Analyzes CloudTrail, VPC Flow Logs, DNS logs, and S3 access logs 24/7 without performance impact.
  name: Continuous Monitoring
- description: Automatically prioritizes findings by severity (Low, Medium, High) for efficient response.
  name: Finding Prioritization
- description: Scans EC2 instance volumes and S3 objects for malware and known threats.
  name: Malware Protection
finops:
- name: Amazon Guardduty Finops
  service_category: API
  slug: amazon-guardduty-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Automatically send GuardDuty findings to Security Hub for centralized security management.
  name: AWS Security Hub
- description: Trigger automated responses to findings using EventBridge rules and Lambda functions.
  name: Amazon EventBridge
- description: Enable GuardDuty organization-wide for centralized multi-account threat monitoring.
  name: AWS Organizations
- description: Investigate GuardDuty findings in depth using Detective for root cause analysis.
  name: Amazon Detective
- description: Combine with Macie for comprehensive data security and threat detection.
  name: Amazon Macie
json_schemas:
- name: Amazon GuardDuty Finding
  property_count: 12
  slug: amazon-guardduty
- name: AcceptAdministratorInvitationRequest
  property_count: 2
  slug: guardduty-accept-administrator-invitation-request
- name: AcceptAdministratorInvitationResponse
  property_count: 0
  slug: guardduty-accept-administrator-invitation-response
- name: AcceptInvitationRequest
  property_count: 2
  slug: guardduty-accept-invitation-request
- name: AcceptInvitationResponse
  property_count: 0
  slug: guardduty-accept-invitation-response
- name: AccessControlList
  property_count: 2
  slug: guardduty-access-control-list
- name: AccessKeyDetails
  property_count: 4
  slug: guardduty-access-key-details
- name: AccountDetail
  property_count: 2
  slug: guardduty-account-detail
- name: AccountDetails
  property_count: 0
  slug: guardduty-account-details
- name: AccountFreeTrialInfo
  property_count: 3
  slug: guardduty-account-free-trial-info
- name: AccountFreeTrialInfos
  property_count: 0
  slug: guardduty-account-free-trial-infos
- name: AccountId
  property_count: 0
  slug: guardduty-account-id
- name: AccountIds
  property_count: 0
  slug: guardduty-account-ids
- name: AccountLevelPermissions
  property_count: 1
  slug: guardduty-account-level-permissions
- name: Action
  property_count: 7
  slug: guardduty-action
- name: AddonDetails
  property_count: 2
  slug: guardduty-addon-details
- name: AdminAccount
  property_count: 2
  slug: guardduty-admin-account
- name: AdminAccounts
  property_count: 0
  slug: guardduty-admin-accounts
- name: AdminStatus
  property_count: 0
  slug: guardduty-admin-status
- name: Administrator
  property_count: 4
  slug: guardduty-administrator
- name: AffectedResources
  property_count: 0
  slug: guardduty-affected-resources
- name: ArchiveFindingsRequest
  property_count: 1
  slug: guardduty-archive-findings-request
- name: ArchiveFindingsResponse
  property_count: 0
  slug: guardduty-archive-findings-response
- name: AutoEnableMembers
  property_count: 0
  slug: guardduty-auto-enable-members
- name: AwsApiCallAction
  property_count: 9
  slug: guardduty-aws-api-call-action
- name: BadRequestException
  property_count: 0
  slug: guardduty-bad-request-exception
- name: BlockPublicAccess
  property_count: 4
  slug: guardduty-block-public-access
- name: Boolean
  property_count: 0
  slug: guardduty-boolean
- name: BucketLevelPermissions
  property_count: 3
  slug: guardduty-bucket-level-permissions
- name: BucketPolicy
  property_count: 2
  slug: guardduty-bucket-policy
- name: City
  property_count: 1
  slug: guardduty-city
- name: ClientToken
  property_count: 0
  slug: guardduty-client-token
- name: CloudTrailConfigurationResult
  property_count: 1
  slug: guardduty-cloud-trail-configuration-result
- name: Condition
  property_count: 12
  slug: guardduty-condition
- name: Container
  property_count: 7
  slug: guardduty-container
- name: Containers
  property_count: 0
  slug: guardduty-containers
- name: CountByCoverageStatus
  property_count: 0
  slug: guardduty-count-by-coverage-status
- name: CountByResourceType
  property_count: 0
  slug: guardduty-count-by-resource-type
- name: CountBySeverity
  property_count: 0
  slug: guardduty-count-by-severity
- name: Country
  property_count: 2
  slug: guardduty-country
- name: CoverageEksClusterDetails
  property_count: 4
  slug: guardduty-coverage-eks-cluster-details
- name: CoverageFilterCondition
  property_count: 2
  slug: guardduty-coverage-filter-condition
- name: CoverageFilterCriteria
  property_count: 1
  slug: guardduty-coverage-filter-criteria
- name: CoverageFilterCriterionKey
  property_count: 0
  slug: guardduty-coverage-filter-criterion-key
- name: CoverageFilterCriterionList
  property_count: 0
  slug: guardduty-coverage-filter-criterion-list
- name: CoverageFilterCriterion
  property_count: 2
  slug: guardduty-coverage-filter-criterion
- name: CoverageResourceDetails
  property_count: 2
  slug: guardduty-coverage-resource-details
- name: CoverageResource
  property_count: 7
  slug: guardduty-coverage-resource
- name: CoverageResources
  property_count: 0
  slug: guardduty-coverage-resources
- name: CoverageSortCriteria
  property_count: 2
  slug: guardduty-coverage-sort-criteria
- name: CoverageSortKey
  property_count: 0
  slug: guardduty-coverage-sort-key
- name: CoverageStatistics
  property_count: 2
  slug: guardduty-coverage-statistics
- name: CoverageStatisticsTypeList
  property_count: 0
  slug: guardduty-coverage-statistics-type-list
- name: CoverageStatisticsType
  property_count: 0
  slug: guardduty-coverage-statistics-type
- name: CoverageStatus
  property_count: 0
  slug: guardduty-coverage-status
- name: CreateDetectorRequest
  property_count: 6
  slug: guardduty-create-detector-request
- name: CreateDetectorResponse
  property_count: 2
  slug: guardduty-create-detector-response
- name: CreateFilterRequest
  property_count: 7
  slug: guardduty-create-filter-request
- name: CreateFilterResponse
  property_count: 1
  slug: guardduty-create-filter-response
- name: CreateIPSetRequest
  property_count: 6
  slug: guardduty-create-ip-set-request
- name: CreateIPSetResponse
  property_count: 1
  slug: guardduty-create-ip-set-response
- name: CreateMembersRequest
  property_count: 1
  slug: guardduty-create-members-request
- name: CreateMembersResponse
  property_count: 1
  slug: guardduty-create-members-response
- name: CreatePublishingDestinationRequest
  property_count: 3
  slug: guardduty-create-publishing-destination-request
- name: CreatePublishingDestinationResponse
  property_count: 1
  slug: guardduty-create-publishing-destination-response
- name: CreateSampleFindingsRequest
  property_count: 1
  slug: guardduty-create-sample-findings-request
- name: CreateSampleFindingsResponse
  property_count: 0
  slug: guardduty-create-sample-findings-response
- name: CreateThreatIntelSetRequest
  property_count: 6
  slug: guardduty-create-threat-intel-set-request
- name: CreateThreatIntelSetResponse
  property_count: 1
  slug: guardduty-create-threat-intel-set-response
- name: CriterionKey
  property_count: 0
  slug: guardduty-criterion-key
- name: Criterion
  property_count: 0
  slug: guardduty-criterion
- name: DataSourceConfigurationsResult
  property_count: 6
  slug: guardduty-data-source-configurations-result
- name: DataSourceConfigurations
  property_count: 3
  slug: guardduty-data-source-configurations
- name: DataSourceFreeTrial
  property_count: 1
  slug: guardduty-data-source-free-trial
- name: DataSourceList
  property_count: 0
  slug: guardduty-data-source-list
- name: DataSource
  property_count: 0
  slug: guardduty-data-source
- name: DataSourceStatus
  property_count: 0
  slug: guardduty-data-source-status
- name: DataSourcesFreeTrial
  property_count: 6
  slug: guardduty-data-sources-free-trial
- name: DeclineInvitationsRequest
  property_count: 1
  slug: guardduty-decline-invitations-request
- name: DeclineInvitationsResponse
  property_count: 1
  slug: guardduty-decline-invitations-response
- name: DefaultServerSideEncryption
  property_count: 2
  slug: guardduty-default-server-side-encryption
- name: DeleteDetectorRequest
  property_count: 0
  slug: guardduty-delete-detector-request
- name: DeleteDetectorResponse
  property_count: 0
  slug: guardduty-delete-detector-response
- name: DeleteFilterRequest
  property_count: 0
  slug: guardduty-delete-filter-request
- name: DeleteFilterResponse
  property_count: 0
  slug: guardduty-delete-filter-response
- name: DeleteInvitationsRequest
  property_count: 1
  slug: guardduty-delete-invitations-request
- name: DeleteInvitationsResponse
  property_count: 1
  slug: guardduty-delete-invitations-response
- name: DeleteIPSetRequest
  property_count: 0
  slug: guardduty-delete-ip-set-request
- name: DeleteIPSetResponse
  property_count: 0
  slug: guardduty-delete-ip-set-response
- name: DeleteMembersRequest
  property_count: 1
  slug: guardduty-delete-members-request
- name: DeleteMembersResponse
  property_count: 1
  slug: guardduty-delete-members-response
- name: DeletePublishingDestinationRequest
  property_count: 0
  slug: guardduty-delete-publishing-destination-request
- name: DeletePublishingDestinationResponse
  property_count: 0
  slug: guardduty-delete-publishing-destination-response
- name: DeleteThreatIntelSetRequest
  property_count: 0
  slug: guardduty-delete-threat-intel-set-request
- name: DeleteThreatIntelSetResponse
  property_count: 0
  slug: guardduty-delete-threat-intel-set-response
- name: DescribeMalwareScansRequest
  property_count: 4
  slug: guardduty-describe-malware-scans-request
- name: DescribeMalwareScansResponse
  property_count: 2
  slug: guardduty-describe-malware-scans-response
- name: DescribeOrganizationConfigurationRequest
  property_count: 0
  slug: guardduty-describe-organization-configuration-request
- name: DescribeOrganizationConfigurationResponse
  property_count: 6
  slug: guardduty-describe-organization-configuration-response
- name: DescribePublishingDestinationRequest
  property_count: 0
  slug: guardduty-describe-publishing-destination-request
- name: DescribePublishingDestinationResponse
  property_count: 5
  slug: guardduty-describe-publishing-destination-response
- name: DestinationProperties
  property_count: 2
  slug: guardduty-destination-properties
- name: Destination
  property_count: 3
  slug: guardduty-destination
- name: DestinationType
  property_count: 0
  slug: guardduty-destination-type
- name: Destinations
  property_count: 0
  slug: guardduty-destinations
- name: DetectorAdditionalConfigurationResult
  property_count: 3
  slug: guardduty-detector-additional-configuration-result
- name: DetectorAdditionalConfigurationResults
  property_count: 0
  slug: guardduty-detector-additional-configuration-results
- name: DetectorAdditionalConfiguration
  property_count: 2
  slug: guardduty-detector-additional-configuration
- name: DetectorAdditionalConfigurations
  property_count: 0
  slug: guardduty-detector-additional-configurations
- name: DetectorFeatureConfigurationResult
  property_count: 4
  slug: guardduty-detector-feature-configuration-result
- name: DetectorFeatureConfiguration
  property_count: 3
  slug: guardduty-detector-feature-configuration
- name: DetectorFeatureConfigurationsResults
  property_count: 0
  slug: guardduty-detector-feature-configurations-results
- name: DetectorFeatureConfigurations
  property_count: 0
  slug: guardduty-detector-feature-configurations
- name: DetectorFeatureResult
  property_count: 0
  slug: guardduty-detector-feature-result
- name: DetectorFeature
  property_count: 0
  slug: guardduty-detector-feature
- name: DetectorId
  property_count: 0
  slug: guardduty-detector-id
- name: DetectorIds
  property_count: 0
  slug: guardduty-detector-ids
- name: DetectorStatus
  property_count: 0
  slug: guardduty-detector-status
- name: DisableOrganizationAdminAccountRequest
  property_count: 1
  slug: guardduty-disable-organization-admin-account-request
- name: DisableOrganizationAdminAccountResponse
  property_count: 0
  slug: guardduty-disable-organization-admin-account-response
- name: DisassociateFromAdministratorAccountRequest
  property_count: 0
  slug: guardduty-disassociate-from-administrator-account-request
- name: DisassociateFromAdministratorAccountResponse
  property_count: 0
  slug: guardduty-disassociate-from-administrator-account-response
- name: DisassociateFromMasterAccountRequest
  property_count: 0
  slug: guardduty-disassociate-from-master-account-request
- name: DisassociateFromMasterAccountResponse
  property_count: 0
  slug: guardduty-disassociate-from-master-account-response
- name: DisassociateMembersRequest
  property_count: 1
  slug: guardduty-disassociate-members-request
- name: DisassociateMembersResponse
  property_count: 1
  slug: guardduty-disassociate-members-response
- name: DNSLogsConfigurationResult
  property_count: 1
  slug: guardduty-dns-logs-configuration-result
- name: DnsRequestAction
  property_count: 3
  slug: guardduty-dns-request-action
- name: DomainDetails
  property_count: 1
  slug: guardduty-domain-details
- name: Double
  property_count: 0
  slug: guardduty-double
- name: EbsSnapshotPreservation
  property_count: 0
  slug: guardduty-ebs-snapshot-preservation
- name: EbsVolumeDetails
  property_count: 2
  slug: guardduty-ebs-volume-details
- name: EbsVolumeScanDetails
  property_count: 6
  slug: guardduty-ebs-volume-scan-details
- name: EbsVolumesResult
  property_count: 2
  slug: guardduty-ebs-volumes-result
- name: EcsClusterDetails
  property_count: 8
  slug: guardduty-ecs-cluster-details
- name: EcsTaskDetails
  property_count: 10
  slug: guardduty-ecs-task-details
- name: EksClusterDetails
  property_count: 6
  slug: guardduty-eks-cluster-details
- name: Email
  property_count: 0
  slug: guardduty-email
- name: EnableOrganizationAdminAccountRequest
  property_count: 1
  slug: guardduty-enable-organization-admin-account-request
- name: EnableOrganizationAdminAccountResponse
  property_count: 0
  slug: guardduty-enable-organization-admin-account-response
- name: Eq
  property_count: 0
  slug: guardduty-eq
- name: Equals
  property_count: 0
  slug: guardduty-equals
- name: Evidence
  property_count: 1
  slug: guardduty-evidence
- name: FeatureAdditionalConfiguration
  property_count: 0
  slug: guardduty-feature-additional-configuration
- name: FeatureStatus
  property_count: 0
  slug: guardduty-feature-status
- name: Feedback
  property_count: 0
  slug: guardduty-feedback
- name: FilePaths
  property_count: 0
  slug: guardduty-file-paths
- name: FilterAction
  property_count: 0
  slug: guardduty-filter-action
- name: FilterCondition
  property_count: 3
  slug: guardduty-filter-condition
- name: FilterCriteria
  property_count: 1
  slug: guardduty-filter-criteria
- name: FilterCriterionList
  property_count: 0
  slug: guardduty-filter-criterion-list
- name: FilterCriterion
  property_count: 2
  slug: guardduty-filter-criterion
- name: FilterDescription
  property_count: 0
  slug: guardduty-filter-description
- name: FilterName
  property_count: 0
  slug: guardduty-filter-name
- name: FilterNames
  property_count: 0
  slug: guardduty-filter-names
- name: FilterRank
  property_count: 0
  slug: guardduty-filter-rank
- name: FindingCriteria
  property_count: 1
  slug: guardduty-finding-criteria
- name: FindingId
  property_count: 0
  slug: guardduty-finding-id
- name: FindingIds
  property_count: 0
  slug: guardduty-finding-ids
- name: FindingPublishingFrequency
  property_count: 0
  slug: guardduty-finding-publishing-frequency
- name: Finding
  property_count: 15
  slug: guardduty-finding
- name: FindingStatisticType
  property_count: 0
  slug: guardduty-finding-statistic-type
- name: FindingStatisticTypes
  property_count: 0
  slug: guardduty-finding-statistic-types
- name: FindingStatistics
  property_count: 1
  slug: guardduty-finding-statistics
- name: FindingType
  property_count: 0
  slug: guardduty-finding-type
- name: FindingTypes
  property_count: 0
  slug: guardduty-finding-types
- name: Findings
  property_count: 0
  slug: guardduty-findings
- name: FlagsList
  property_count: 0
  slug: guardduty-flags-list
- name: FlowLogsConfigurationResult
  property_count: 1
  slug: guardduty-flow-logs-configuration-result
- name: FreeTrialFeatureConfigurationResult
  property_count: 2
  slug: guardduty-free-trial-feature-configuration-result
- name: FreeTrialFeatureConfigurationsResults
  property_count: 0
  slug: guardduty-free-trial-feature-configurations-results
- name: FreeTrialFeatureResult
  property_count: 0
  slug: guardduty-free-trial-feature-result
- name: GeoLocation
  property_count: 2
  slug: guardduty-geo-location
- name: GetAdministratorAccountRequest
  property_count: 0
  slug: guardduty-get-administrator-account-request
- name: GetAdministratorAccountResponse
  property_count: 1
  slug: guardduty-get-administrator-account-response
- name: GetCoverageStatisticsRequest
  property_count: 2
  slug: guardduty-get-coverage-statistics-request
- name: GetCoverageStatisticsResponse
  property_count: 1
  slug: guardduty-get-coverage-statistics-response
- name: GetDetectorRequest
  property_count: 0
  slug: guardduty-get-detector-request
- name: GetDetectorResponse
  property_count: 8
  slug: guardduty-get-detector-response
- name: GetFilterRequest
  property_count: 0
  slug: guardduty-get-filter-request
- name: GetFilterResponse
  property_count: 6
  slug: guardduty-get-filter-response
- name: GetFindingsRequest
  property_count: 2
  slug: guardduty-get-findings-request
- name: GetFindingsResponse
  property_count: 1
  slug: guardduty-get-findings-response
- name: GetFindingsStatisticsRequest
  property_count: 2
  slug: guardduty-get-findings-statistics-request
- name: GetFindingsStatisticsResponse
  property_count: 1
  slug: guardduty-get-findings-statistics-response
- name: GetInvitationsCountRequest
  property_count: 0
  slug: guardduty-get-invitations-count-request
- name: GetInvitationsCountResponse
  property_count: 1
  slug: guardduty-get-invitations-count-response
- name: GetIPSetRequest
  property_count: 0
  slug: guardduty-get-ip-set-request
- name: GetIPSetResponse
  property_count: 5
  slug: guardduty-get-ip-set-response
- name: GetMalwareScanSettingsRequest
  property_count: 0
  slug: guardduty-get-malware-scan-settings-request
- name: GetMalwareScanSettingsResponse
  property_count: 2
  slug: guardduty-get-malware-scan-settings-response
- name: GetMasterAccountRequest
  property_count: 0
  slug: guardduty-get-master-account-request
- name: GetMasterAccountResponse
  property_count: 1
  slug: guardduty-get-master-account-response
- name: GetMemberDetectorsRequest
  property_count: 1
  slug: guardduty-get-member-detectors-request
- name: GetMemberDetectorsResponse
  property_count: 2
  slug: guardduty-get-member-detectors-response
- name: GetMembersRequest
  property_count: 1
  slug: guardduty-get-members-request
- name: GetMembersResponse
  property_count: 2
  slug: guardduty-get-members-response
- name: GetRemainingFreeTrialDaysRequest
  property_count: 1
  slug: guardduty-get-remaining-free-trial-days-request
- name: GetRemainingFreeTrialDaysResponse
  property_count: 2
  slug: guardduty-get-remaining-free-trial-days-response
- name: GetThreatIntelSetRequest
  property_count: 0
  slug: guardduty-get-threat-intel-set-request
- name: GetThreatIntelSetResponse
  property_count: 5
  slug: guardduty-get-threat-intel-set-response
- name: GetUsageStatisticsRequest
  property_count: 5
  slug: guardduty-get-usage-statistics-request
- name: GetUsageStatisticsResponse
  property_count: 2
  slug: guardduty-get-usage-statistics-response
- name: Groups
  property_count: 0
  slug: guardduty-groups
- name: GuardDutyArn
  property_count: 0
  slug: guardduty-guard-duty-arn
- name: HighestSeverityThreatDetails
  property_count: 3
  slug: guardduty-highest-severity-threat-details
- name: HostPath
  property_count: 1
  slug: guardduty-host-path
- name: IamInstanceProfile
  property_count: 2
  slug: guardduty-iam-instance-profile
- name: InstanceArn
  property_count: 0
  slug: guardduty-instance-arn
- name: InstanceDetails
  property_count: 13
  slug: guardduty-instance-details
- name: Integer
  property_count: 0
  slug: guardduty-integer
- name: IntegerValueWithMax
  property_count: 0
  slug: guardduty-integer-value-with-max
- name: InternalServerErrorException
  property_count: 0
  slug: guardduty-internal-server-error-exception
- name: Invitation
  property_count: 4
  slug: guardduty-invitation
- name: Invitations
  property_count: 0
  slug: guardduty-invitations
- name: InviteMembersRequest
  property_count: 3
  slug: guardduty-invite-members-request
- name: InviteMembersResponse
  property_count: 1
  slug: guardduty-invite-members-response
- name: IpSetFormat
  property_count: 0
  slug: guardduty-ip-set-format
- name: IpSetIds
  property_count: 0
  slug: guardduty-ip-set-ids
- name: IpSetStatus
  property_count: 0
  slug: guardduty-ip-set-status
- name: Ipv6Addresses
  property_count: 0
  slug: guardduty-ipv6-addresses
- name: KubernetesApiCallAction
  property_count: 7
  slug: guardduty-kubernetes-api-call-action
- name: KubernetesAuditLogsConfigurationResult
  property_count: 1
  slug: guardduty-kubernetes-audit-logs-configuration-result
- name: KubernetesAuditLogsConfiguration
  property_count: 1
  slug: guardduty-kubernetes-audit-logs-configuration
- name: KubernetesConfigurationResult
  property_count: 1
  slug: guardduty-kubernetes-configuration-result
- name: KubernetesConfiguration
  property_count: 1
  slug: guardduty-kubernetes-configuration
- name: KubernetesDataSourceFreeTrial
  property_count: 1
  slug: guardduty-kubernetes-data-source-free-trial
- name: KubernetesDetails
  property_count: 2
  slug: guardduty-kubernetes-details
- name: KubernetesUserDetails
  property_count: 3
  slug: guardduty-kubernetes-user-details
- name: KubernetesWorkloadDetails
  property_count: 7
  slug: guardduty-kubernetes-workload-details
- name: LambdaDetails
  property_count: 9
  slug: guardduty-lambda-details
- name: LineageObject
  property_count: 9
  slug: guardduty-lineage-object
- name: Lineage
  property_count: 0
  slug: guardduty-lineage
- name: ListCoverageRequest
  property_count: 4
  slug: guardduty-list-coverage-request
- name: ListCoverageResponse
  property_count: 2
  slug: guardduty-list-coverage-response
- name: ListDetectorsRequest
  property_count: 0
  slug: guardduty-list-detectors-request
- name: ListDetectorsResponse
  property_count: 2
  slug: guardduty-list-detectors-response
- name: ListFiltersRequest
  property_count: 0
  slug: guardduty-list-filters-request
- name: ListFiltersResponse
  property_count: 2
  slug: guardduty-list-filters-response
- name: ListFindingsRequest
  property_count: 4
  slug: guardduty-list-findings-request
- name: ListFindingsResponse
  property_count: 2
  slug: guardduty-list-findings-response
- name: ListInvitationsRequest
  property_count: 0
  slug: guardduty-list-invitations-request
- name: ListInvitationsResponse
  property_count: 2
  slug: guardduty-list-invitations-response
- name: ListIPSetsRequest
  property_count: 0
  slug: guardduty-list-ip-sets-request
- name: ListIPSetsResponse
  property_count: 2
  slug: guardduty-list-ip-sets-response
- name: ListMembersRequest
  property_count: 0
  slug: guardduty-list-members-request
- name: ListMembersResponse
  property_count: 2
  slug: guardduty-list-members-response
- name: ListOrganizationAdminAccountsRequest
  property_count: 0
  slug: guardduty-list-organization-admin-accounts-request
- name: ListOrganizationAdminAccountsResponse
  property_count: 2
  slug: guardduty-list-organization-admin-accounts-response
- name: ListPublishingDestinationsRequest
  property_count: 0
  slug: guardduty-list-publishing-destinations-request
- name: ListPublishingDestinationsResponse
  property_count: 2
  slug: guardduty-list-publishing-destinations-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: guardduty-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: guardduty-list-tags-for-resource-response
- name: ListThreatIntelSetsRequest
  property_count: 0
  slug: guardduty-list-threat-intel-sets-request
- name: ListThreatIntelSetsResponse
  property_count: 2
  slug: guardduty-list-threat-intel-sets-response
- name: LocalIpDetails
  property_count: 1
  slug: guardduty-local-ip-details
- name: LocalPortDetails
  property_count: 2
  slug: guardduty-local-port-details
- name: Location
  property_count: 0
  slug: guardduty-location
- name: LoginAttribute
  property_count: 4
  slug: guardduty-login-attribute
- name: LoginAttributes
  property_count: 0
  slug: guardduty-login-attributes
- name: Long
  property_count: 0
  slug: guardduty-long
- name: LongValue
  property_count: 0
  slug: guardduty-long-value
- name: MalwareProtectionConfigurationResult
  property_count: 2
  slug: guardduty-malware-protection-configuration-result
- name: MalwareProtectionConfiguration
  property_count: 1
  slug: guardduty-malware-protection-configuration
- name: MalwareProtectionDataSourceFreeTrial
  property_count: 1
  slug: guardduty-malware-protection-data-source-free-trial
- name: MapEquals
  property_count: 0
  slug: guardduty-map-equals
- name: Master
  property_count: 4
  slug: guardduty-master
- name: MaxResults
  property_count: 0
  slug: guardduty-max-results
- name: MemberAdditionalConfigurationResult
  property_count: 3
  slug: guardduty-member-additional-configuration-result
- name: MemberAdditionalConfigurationResults
  property_count: 0
  slug: guardduty-member-additional-configuration-results
- name: MemberAdditionalConfiguration
  property_count: 2
  slug: guardduty-member-additional-configuration
- name: MemberAdditionalConfigurations
  property_count: 0
  slug: guardduty-member-additional-configurations
- name: MemberDataSourceConfiguration
  property_count: 3
  slug: guardduty-member-data-source-configuration
- name: MemberDataSourceConfigurations
  property_count: 0
  slug: guardduty-member-data-source-configurations
- name: MemberFeaturesConfigurationResult
  property_count: 4
  slug: guardduty-member-features-configuration-result
- name: MemberFeaturesConfiguration
  property_count: 3
  slug: guardduty-member-features-configuration
- name: MemberFeaturesConfigurationsResults
  property_count: 0
  slug: guardduty-member-features-configurations-results
- name: MemberFeaturesConfigurations
  property_count: 0
  slug: guardduty-member-features-configurations
- name: Member
  property_count: 8
  slug: guardduty-member
- name: Members
  property_count: 0
  slug: guardduty-members
- name: MemoryRegionsList
  property_count: 0
  slug: guardduty-memory-regions-list
- name: Name
  property_count: 0
  slug: guardduty-name
- name: Neq
  property_count: 0
  slug: guardduty-neq
- name: NetworkConnectionAction
  property_count: 7
  slug: guardduty-network-connection-action
- name: NetworkInterface
  property_count: 10
  slug: guardduty-network-interface
- name: NetworkInterfaces
  property_count: 0
  slug: guardduty-network-interfaces
- name: NonEmptyString
  property_count: 0
  slug: guardduty-non-empty-string
- name: NotEquals
  property_count: 0
  slug: guardduty-not-equals
- name: OrderBy
  property_count: 0
  slug: guardduty-order-by
- name: OrgFeatureAdditionalConfiguration
  property_count: 0
  slug: guardduty-org-feature-additional-configuration
- name: OrgFeature
  property_count: 0
  slug: guardduty-org-feature
- name: OrgFeatureStatus
  property_count: 0
  slug: guardduty-org-feature-status
- name: OrganizationAdditionalConfigurationResult
  property_count: 2
  slug: guardduty-organization-additional-configuration-result
- name: OrganizationAdditionalConfigurationResults
  property_count: 0
  slug: guardduty-organization-additional-configuration-results
- name: OrganizationAdditionalConfiguration
  property_count: 2
  slug: guardduty-organization-additional-configuration
- name: OrganizationAdditionalConfigurations
  property_count: 0
  slug: guardduty-organization-additional-configurations
- name: OrganizationDataSourceConfigurationsResult
  property_count: 3
  slug: guardduty-organization-data-source-configurations-result
- name: OrganizationDataSourceConfigurations
  property_count: 3
  slug: guardduty-organization-data-source-configurations
- name: OrganizationEbsVolumesResult
  property_count: 1
  slug: guardduty-organization-ebs-volumes-result
- name: OrganizationEbsVolumes
  property_count: 1
  slug: guardduty-organization-ebs-volumes
- name: OrganizationFeatureConfigurationResult
  property_count: 3
  slug: guardduty-organization-feature-configuration-result
- name: OrganizationFeatureConfiguration
  property_count: 3
  slug: guardduty-organization-feature-configuration
- name: OrganizationFeaturesConfigurationsResults
  property_count: 0
  slug: guardduty-organization-features-configurations-results
- name: OrganizationFeaturesConfigurations
  property_count: 0
  slug: guardduty-organization-features-configurations
- name: OrganizationKubernetesAuditLogsConfigurationResult
  property_count: 1
  slug: guardduty-organization-kubernetes-audit-logs-configuration-result
- name: OrganizationKubernetesAuditLogsConfiguration
  property_count: 1
  slug: guardduty-organization-kubernetes-audit-logs-configuration
- name: OrganizationKubernetesConfigurationResult
  property_count: 1
  slug: guardduty-organization-kubernetes-configuration-result
- name: OrganizationKubernetesConfiguration
  property_count: 1
  slug: guardduty-organization-kubernetes-configuration
- name: OrganizationMalwareProtectionConfigurationResult
  property_count: 1
  slug: guardduty-organization-malware-protection-configuration-result
- name: OrganizationMalwareProtectionConfiguration
  property_count: 1
  slug: guardduty-organization-malware-protection-configuration
- name: OrganizationS3LogsConfigurationResult
  property_count: 1
  slug: guardduty-organization-s3-logs-configuration-result
- name: OrganizationS3LogsConfiguration
  property_count: 1
  slug: guardduty-organization-s3-logs-configuration
- name: OrganizationScanEc2InstanceWithFindingsResult
  property_count: 1
  slug: guardduty-organization-scan-ec2-instance-with-findings-result
- name: OrganizationScanEc2InstanceWithFindings
  property_count: 1
  slug: guardduty-organization-scan-ec2-instance-with-findings
- name: Organization
  property_count: 4
  slug: guardduty-organization
- name: Owner
  property_count: 1
  slug: guardduty-owner
- name: PermissionConfiguration
  property_count: 2
  slug: guardduty-permission-configuration
- name: PortProbeAction
  property_count: 2
  slug: guardduty-port-probe-action
- name: PortProbeDetail
  property_count: 3
  slug: guardduty-port-probe-detail
- name: PortProbeDetails
  property_count: 0
  slug: guardduty-port-probe-details
- name: PositiveLong
  property_count: 0
  slug: guardduty-positive-long
- name: PrivateIpAddressDetails
  property_count: 2
  slug: guardduty-private-ip-address-details
- name: PrivateIpAddresses
  property_count: 0
  slug: guardduty-private-ip-addresses
- name: ProcessDetails
  property_count: 13
  slug: guardduty-process-details
- name: ProductCode
  property_count: 2
  slug: guardduty-product-code
- name: ProductCodes
  property_count: 0
  slug: guardduty-product-codes
- name: PublicAccess
  property_count: 2
  slug: guardduty-public-access
- name: PublishingStatus
  property_count: 0
  slug: guardduty-publishing-status
- name: RdsDbInstanceDetails
  property_count: 6
  slug: guardduty-rds-db-instance-details
- name: RdsDbUserDetails
  property_count: 5
  slug: guardduty-rds-db-user-details
- name: RdsLoginAttemptAction
  property_count: 2
  slug: guardduty-rds-login-attempt-action
- name: RemoteAccountDetails
  property_count: 2
  slug: guardduty-remote-account-details
- name: RemoteIpDetails
  property_count: 5
  slug: guardduty-remote-ip-details
- name: RemotePortDetails
  property_count: 2
  slug: guardduty-remote-port-details
- name: ResourceDetails
  property_count: 1
  slug: guardduty-resource-details
- name: ResourceList
  property_count: 0
  slug: guardduty-resource-list
- name: Resource
  property_count: 12
  slug: guardduty-resource
- name: ResourceType
  property_count: 0
  slug: guardduty-resource-type
- name: RuntimeContext
  property_count: 20
  slug: guardduty-runtime-context
- name: RuntimeDetails
  property_count: 2
  slug: guardduty-runtime-details
- name: S3BucketDetail
  property_count: 8
  slug: guardduty-s3-bucket-detail
- name: S3BucketDetails
  property_count: 0
  slug: guardduty-s3-bucket-details
- name: S3LogsConfigurationResult
  property_count: 1
  slug: guardduty-s3-logs-configuration-result
- name: S3LogsConfiguration
  property_count: 1
  slug: guardduty-s3-logs-configuration
- name: ScanConditionPair
  property_count: 2
  slug: guardduty-scan-condition-pair
- name: ScanCondition
  property_count: 1
  slug: guardduty-scan-condition
- name: ScanCriterionKey
  property_count: 0
  slug: guardduty-scan-criterion-key
- name: ScanCriterion
  property_count: 0
  slug: guardduty-scan-criterion
- name: ScanDetections
  property_count: 4
  slug: guardduty-scan-detections
- name: ScanEc2InstanceWithFindingsResult
  property_count: 1
  slug: guardduty-scan-ec2-instance-with-findings-result
- name: ScanEc2InstanceWithFindings
  property_count: 1
  slug: guardduty-scan-ec2-instance-with-findings
- name: ScanFilePath
  property_count: 4
  slug: guardduty-scan-file-path
- name: ScanResourceCriteria
  property_count: 2
  slug: guardduty-scan-resource-criteria
- name: ScanResultDetails
  property_count: 1
  slug: guardduty-scan-result-details
- name: ScanResult
  property_count: 0
  slug: guardduty-scan-result
- name: Scan
  property_count: 14
  slug: guardduty-scan
- name: ScanStatus
  property_count: 0
  slug: guardduty-scan-status
- name: ScanThreatName
  property_count: 4
  slug: guardduty-scan-threat-name
- name: ScanThreatNames
  property_count: 0
  slug: guardduty-scan-threat-names
- name: ScannedItemCount
  property_count: 3
  slug: guardduty-scanned-item-count
- name: Scans
  property_count: 0
  slug: guardduty-scans
- name: SecurityContext
  property_count: 1
  slug: guardduty-security-context
- name: SecurityGroup
  property_count: 2
  slug: guardduty-security-group
- name: SecurityGroups
  property_count: 0
  slug: guardduty-security-groups
- name: ServiceAdditionalInfo
  property_count: 2
  slug: guardduty-service-additional-info
- name: Service
  property_count: 14
  slug: guardduty-service
- name: SortCriteria
  property_count: 2
  slug: guardduty-sort-criteria
- name: SourceIps
  property_count: 0
  slug: guardduty-source-ips
- name: Sources
  property_count: 0
  slug: guardduty-sources
- name: StartMonitoringMembersRequest
  property_count: 1
  slug: guardduty-start-monitoring-members-request
- name: StartMonitoringMembersResponse
  property_count: 1
  slug: guardduty-start-monitoring-members-response
- name: StopMonitoringMembersRequest
  property_count: 1
  slug: guardduty-stop-monitoring-members-request
- name: StopMonitoringMembersResponse
  property_count: 1
  slug: guardduty-stop-monitoring-members-response
- name: String
  property_count: 0
  slug: guardduty-string
- name: SubnetIds
  property_count: 0
  slug: guardduty-subnet-ids
- name: TagKeyList
  property_count: 0
  slug: guardduty-tag-key-list
- name: TagKey
  property_count: 0
  slug: guardduty-tag-key
- name: TagMap
  property_count: 0
  slug: guardduty-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: guardduty-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: guardduty-tag-resource-response
- name: Tag
  property_count: 2
  slug: guardduty-tag
- name: TagValue
  property_count: 0
  slug: guardduty-tag-value
- name: Tags
  property_count: 0
  slug: guardduty-tags
- name: ThreatDetectedByName
  property_count: 4
  slug: guardduty-threat-detected-by-name
- name: ThreatIntelSetFormat
  property_count: 0
  slug: guardduty-threat-intel-set-format
- name: ThreatIntelSetIds
  property_count: 0
  slug: guardduty-threat-intel-set-ids
- name: ThreatIntelSetStatus
  property_count: 0
  slug: guardduty-threat-intel-set-status
- name: ThreatIntelligenceDetail
  property_count: 2
  slug: guardduty-threat-intelligence-detail
- name: ThreatIntelligenceDetails
  property_count: 0
  slug: guardduty-threat-intelligence-details
- name: ThreatNames
  property_count: 0
  slug: guardduty-threat-names
- name: ThreatsDetectedItemCount
  property_count: 1
  slug: guardduty-threats-detected-item-count
- name: Timestamp
  property_count: 0
  slug: guardduty-timestamp
- name: Total
  property_count: 2
  slug: guardduty-total
- name: TriggerDetails
  property_count: 2
  slug: guardduty-trigger-details
- name: UnarchiveFindingsRequest
  property_count: 1
  slug: guardduty-unarchive-findings-request
- name: UnarchiveFindingsResponse
  property_count: 0
  slug: guardduty-unarchive-findings-response
- name: UnprocessedAccount
  property_count: 2
  slug: guardduty-unprocessed-account
- name: UnprocessedAccounts
  property_count: 0
  slug: guardduty-unprocessed-accounts
- name: UnprocessedDataSourcesResult
  property_count: 1
  slug: guardduty-unprocessed-data-sources-result
- name: UntagResourceRequest
  property_count: 0
  slug: guardduty-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: guardduty-untag-resource-response
- name: UpdateDetectorRequest
  property_count: 4
  slug: guardduty-update-detector-request
- name: UpdateDetectorResponse
  property_count: 0
  slug: guardduty-update-detector-response
- name: UpdateFilterRequest
  property_count: 4
  slug: guardduty-update-filter-request
- name: UpdateFilterResponse
  property_count: 1
  slug: guardduty-update-filter-response
- name: UpdateFindingsFeedbackRequest
  property_count: 3
  slug: guardduty-update-findings-feedback-request
- name: UpdateFindingsFeedbackResponse
  property_count: 0
  slug: guardduty-update-findings-feedback-response
- name: UpdateIPSetRequest
  property_count: 3
  slug: guardduty-update-ip-set-request
- name: UpdateIPSetResponse
  property_count: 0
  slug: guardduty-update-ip-set-response
- name: UpdateMalwareScanSettingsRequest
  property_count: 2
  slug: guardduty-update-malware-scan-settings-request
- name: UpdateMalwareScanSettingsResponse
  property_count: 0
  slug: guardduty-update-malware-scan-settings-response
- name: UpdateMemberDetectorsRequest
  property_count: 3
  slug: guardduty-update-member-detectors-request
- name: UpdateMemberDetectorsResponse
  property_count: 1
  slug: guardduty-update-member-detectors-response
- name: UpdateOrganizationConfigurationRequest
  property_count: 4
  slug: guardduty-update-organization-configuration-request
- name: UpdateOrganizationConfigurationResponse
  property_count: 0
  slug: guardduty-update-organization-configuration-response
- name: UpdatePublishingDestinationRequest
  property_count: 1
  slug: guardduty-update-publishing-destination-request
- name: UpdatePublishingDestinationResponse
  property_count: 0
  slug: guardduty-update-publishing-destination-response
- name: UpdateThreatIntelSetRequest
  property_count: 3
  slug: guardduty-update-threat-intel-set-request
- name: UpdateThreatIntelSetResponse
  property_count: 0
  slug: guardduty-update-threat-intel-set-response
- name: UsageAccountResultList
  property_count: 0
  slug: guardduty-usage-account-result-list
- name: UsageAccountResult
  property_count: 2
  slug: guardduty-usage-account-result
- name: UsageCriteria
  property_count: 4
  slug: guardduty-usage-criteria
- name: UsageDataSourceResultList
  property_count: 0
  slug: guardduty-usage-data-source-result-list
- name: UsageDataSourceResult
  property_count: 2
  slug: guardduty-usage-data-source-result
- name: UsageFeatureList
  property_count: 0
  slug: guardduty-usage-feature-list
- name: UsageFeatureResultList
  property_count: 0
  slug: guardduty-usage-feature-result-list
- name: UsageFeatureResult
  property_count: 2
  slug: guardduty-usage-feature-result
- name: UsageFeature
  property_count: 0
  slug: guardduty-usage-feature
- name: UsageResourceResultList
  property_count: 0
  slug: guardduty-usage-resource-result-list
- name: UsageResourceResult
  property_count: 2
  slug: guardduty-usage-resource-result
- name: UsageStatisticType
  property_count: 0
  slug: guardduty-usage-statistic-type
- name: UsageStatistics
  property_count: 5
  slug: guardduty-usage-statistics
- name: VolumeDetail
  property_count: 7
  slug: guardduty-volume-detail
- name: VolumeDetails
  property_count: 0
  slug: guardduty-volume-details
- name: VolumeMount
  property_count: 2
  slug: guardduty-volume-mount
- name: VolumeMounts
  property_count: 0
  slug: guardduty-volume-mounts
- name: Volume
  property_count: 2
  slug: guardduty-volume
- name: Volumes
  property_count: 0
  slug: guardduty-volumes
- name: VpcConfig
  property_count: 3
  slug: guardduty-vpc-config
json_structures:
- name: Amazon Guardduty Structure
  property_count: 12
  slug: amazon-guardduty-structure
- name: Guardduty Accept Administrator Invitation Request Structure
  property_count: 2
  slug: guardduty-accept-administrator-invitation-request-structure
- name: Guardduty Accept Administrator Invitation Response Structure
  property_count: 0
  slug: guardduty-accept-administrator-invitation-response-structure
- name: Guardduty Accept Invitation Request Structure
  property_count: 2
  slug: guardduty-accept-invitation-request-structure
- name: Guardduty Accept Invitation Response Structure
  property_count: 0
  slug: guardduty-accept-invitation-response-structure
- name: Guardduty Access Control List Structure
  property_count: 2
  slug: guardduty-access-control-list-structure
- name: Guardduty Access Key Details Structure
  property_count: 4
  slug: guardduty-access-key-details-structure
- name: Guardduty Account Detail Structure
  property_count: 2
  slug: guardduty-account-detail-structure
- name: Guardduty Account Details Structure
  property_count: 0
  slug: guardduty-account-details-structure
- name: Guardduty Account Free Trial Info Structure
  property_count: 3
  slug: guardduty-account-free-trial-info-structure
- name: Guardduty Account Free Trial Infos Structure
  property_count: 0
  slug: guardduty-account-free-trial-infos-structure
- name: Guardduty Account Id Structure
  property_count: 0
  slug: guardduty-account-id-structure
- name: Guardduty Account Ids Structure
  property_count: 0
  slug: guardduty-account-ids-structure
- name: Guardduty Account Level Permissions Structure
  property_count: 1
  slug: guardduty-account-level-permissions-structure
- name: Guardduty Action Structure
  property_count: 7
  slug: guardduty-action-structure
- name: Guardduty Addon Details Structure
  property_count: 2
  slug: guardduty-addon-details-structure
- name: Guardduty Admin Account Structure
  property_count: 2
  slug: guardduty-admin-account-structure
- name: Guardduty Admin Accounts Structure
  property_count: 0
  slug: guardduty-admin-accounts-structure
- name: Guardduty Admin Status Structure
  property_count: 0
  slug: guardduty-admin-status-structure
- name: Guardduty Administrator Structure
  property_count: 4
  slug: guardduty-administrator-structure
- name: Guardduty Affected Resources Structure
  property_count: 0
  slug: guardduty-affected-resources-structure
- name: Guardduty Archive Findings Request Structure
  property_count: 1
  slug: guardduty-archive-findings-request-structure
- name: Guardduty Archive Findings Response Structure
  property_count: 0
  slug: guardduty-archive-findings-response-structure
- name: Guardduty Auto Enable Members Structure
  property_count: 0
  slug: guardduty-auto-enable-members-structure
- name: Guardduty Aws Api Call Action Structure
  property_count: 9
  slug: guardduty-aws-api-call-action-structure
- name: Guardduty Bad Request Exception Structure
  property_count: 0
  slug: guardduty-bad-request-exception-structure
- name: Guardduty Block Public Access Structure
  property_count: 4
  slug: guardduty-block-public-access-structure
- name: Guardduty Boolean Structure
  property_count: 0
  slug: guardduty-boolean-structure
- name: Guardduty Bucket Level Permissions Structure
  property_count: 3
  slug: guardduty-bucket-level-permissions-structure
- name: Guardduty Bucket Policy Structure
  property_count: 2
  slug: guardduty-bucket-policy-structure
- name: Guardduty City Structure
  property_count: 1
  slug: guardduty-city-structure
- name: Guardduty Client Token Structure
  property_count: 0
  slug: guardduty-client-token-structure
- name: Guardduty Cloud Trail Configuration Result Structure
  property_count: 1
  slug: guardduty-cloud-trail-configuration-result-structure
- name: Guardduty Condition Structure
  property_count: 12
  slug: guardduty-condition-structure
- name: Guardduty Container Structure
  property_count: 7
  slug: guardduty-container-structure
- name: Guardduty Containers Structure
  property_count: 0
  slug: guardduty-containers-structure
- name: Guardduty Count By Coverage Status Structure
  property_count: 0
  slug: guardduty-count-by-coverage-status-structure
- name: Guardduty Count By Resource Type Structure
  property_count: 0
  slug: guardduty-count-by-resource-type-structure
- name: Guardduty Count By Severity Structure
  property_count: 0
  slug: guardduty-count-by-severity-structure
- name: Guardduty Country Structure
  property_count: 2
  slug: guardduty-country-structure
- name: Guardduty Coverage Eks Cluster Details Structure
  property_count: 4
  slug: guardduty-coverage-eks-cluster-details-structure
- name: Guardduty Coverage Filter Condition Structure
  property_count: 2
  slug: guardduty-coverage-filter-condition-structure
- name: Guardduty Coverage Filter Criteria Structure
  property_count: 1
  slug: guardduty-coverage-filter-criteria-structure
- name: Guardduty Coverage Filter Criterion Key Structure
  property_count: 0
  slug: guardduty-coverage-filter-criterion-key-structure
- name: Guardduty Coverage Filter Criterion List Structure
  property_count: 0
  slug: guardduty-coverage-filter-criterion-list-structure
- name: Guardduty Coverage Filter Criterion Structure
  property_count: 2
  slug: guardduty-coverage-filter-criterion-structure
- name: Guardduty Coverage Resource Details Structure
  property_count: 2
  slug: guardduty-coverage-resource-details-structure
- name: Guardduty Coverage Resource Structure
  property_count: 7
  slug: guardduty-coverage-resource-structure
- name: Guardduty Coverage Resources Structure
  property_count: 0
  slug: guardduty-coverage-resources-structure
- name: Guardduty Coverage Sort Criteria Structure
  property_count: 2
  slug: guardduty-coverage-sort-criteria-structure
- name: Guardduty Coverage Sort Key Structure
  property_count: 0
  slug: guardduty-coverage-sort-key-structure
- name: Guardduty Coverage Statistics Structure
  property_count: 2
  slug: guardduty-coverage-statistics-structure
- name: Guardduty Coverage Statistics Type List Structure
  property_count: 0
  slug: guardduty-coverage-statistics-type-list-structure
- name: Guardduty Coverage Statistics Type Structure
  property_count: 0
  slug: guardduty-coverage-statistics-type-structure
- name: Guardduty Coverage Status Structure
  property_count: 0
  slug: guardduty-coverage-status-structure
- name: Guardduty Create Detector Request Structure
  property_count: 6
  slug: guardduty-create-detector-request-structure
- name: Guardduty Create Detector Response Structure
  property_count: 2
  slug: guardduty-create-detector-response-structure
- name: Guardduty Create Filter Request Structure
  property_count: 7
  slug: guardduty-create-filter-request-structure
- name: Guardduty Create Filter Response Structure
  property_count: 1
  slug: guardduty-create-filter-response-structure
- name: Guardduty Create Ip Set Request Structure
  property_count: 6
  slug: guardduty-create-ip-set-request-structure
- name: Guardduty Create Ip Set Response Structure
  property_count: 1
  slug: guardduty-create-ip-set-response-structure
- name: Guardduty Create Members Request Structure
  property_count: 1
  slug: guardduty-create-members-request-structure
- name: Guardduty Create Members Response Structure
  property_count: 1
  slug: guardduty-create-members-response-structure
- name: Guardduty Create Publishing Destination Request Structure
  property_count: 3
  slug: guardduty-create-publishing-destination-request-structure
- name: Guardduty Create Publishing Destination Response Structure
  property_count: 1
  slug: guardduty-create-publishing-destination-response-structure
- name: Guardduty Create Sample Findings Request Structure
  property_count: 1
  slug: guardduty-create-sample-findings-request-structure
- name: Guardduty Create Sample Findings Response Structure
  property_count: 0
  slug: guardduty-create-sample-findings-response-structure
- name: Guardduty Create Threat Intel Set Request Structure
  property_count: 6
  slug: guardduty-create-threat-intel-set-request-structure
- name: Guardduty Create Threat Intel Set Response Structure
  property_count: 1
  slug: guardduty-create-threat-intel-set-response-structure
- name: Guardduty Criterion Key Structure
  property_count: 0
  slug: guardduty-criterion-key-structure
- name: Guardduty Criterion Structure
  property_count: 0
  slug: guardduty-criterion-structure
- name: Guardduty Data Source Configurations Result Structure
  property_count: 6
  slug: guardduty-data-source-configurations-result-structure
- name: Guardduty Data Source Configurations Structure
  property_count: 3
  slug: guardduty-data-source-configurations-structure
- name: Guardduty Data Source Free Trial Structure
  property_count: 1
  slug: guardduty-data-source-free-trial-structure
- name: Guardduty Data Source List Structure
  property_count: 0
  slug: guardduty-data-source-list-structure
- name: Guardduty Data Source Status Structure
  property_count: 0
  slug: guardduty-data-source-status-structure
- name: Guardduty Data Source Structure
  property_count: 0
  slug: guardduty-data-source-structure
- name: Guardduty Data Sources Free Trial Structure
  property_count: 6
  slug: guardduty-data-sources-free-trial-structure
- name: Guardduty Decline Invitations Request Structure
  property_count: 1
  slug: guardduty-decline-invitations-request-structure
- name: Guardduty Decline Invitations Response Structure
  property_count: 1
  slug: guardduty-decline-invitations-response-structure
- name: Guardduty Default Server Side Encryption Structure
  property_count: 2
  slug: guardduty-default-server-side-encryption-structure
- name: Guardduty Delete Detector Request Structure
  property_count: 0
  slug: guardduty-delete-detector-request-structure
- name: Guardduty Delete Detector Response Structure
  property_count: 0
  slug: guardduty-delete-detector-response-structure
- name: Guardduty Delete Filter Request Structure
  property_count: 0
  slug: guardduty-delete-filter-request-structure
- name: Guardduty Delete Filter Response Structure
  property_count: 0
  slug: guardduty-delete-filter-response-structure
- name: Guardduty Delete Invitations Request Structure
  property_count: 1
  slug: guardduty-delete-invitations-request-structure
- name: Guardduty Delete Invitations Response Structure
  property_count: 1
  slug: guardduty-delete-invitations-response-structure
- name: Guardduty Delete Ip Set Request Structure
  property_count: 0
  slug: guardduty-delete-ip-set-request-structure
- name: Guardduty Delete Ip Set Response Structure
  property_count: 0
  slug: guardduty-delete-ip-set-response-structure
- name: Guardduty Delete Members Request Structure
  property_count: 1
  slug: guardduty-delete-members-request-structure
- name: Guardduty Delete Members Response Structure
  property_count: 1
  slug: guardduty-delete-members-response-structure
- name: Guardduty Delete Publishing Destination Request Structure
  property_count: 0
  slug: guardduty-delete-publishing-destination-request-structure
- name: Guardduty Delete Publishing Destination Response Structure
  property_count: 0
  slug: guardduty-delete-publishing-destination-response-structure
- name: Guardduty Delete Threat Intel Set Request Structure
  property_count: 0
  slug: guardduty-delete-threat-intel-set-request-structure
- name: Guardduty Delete Threat Intel Set Response Structure
  property_count: 0
  slug: guardduty-delete-threat-intel-set-response-structure
- name: Guardduty Describe Malware Scans Request Structure
  property_count: 4
  slug: guardduty-describe-malware-scans-request-structure
- name: Guardduty Describe Malware Scans Response Structure
  property_count: 2
  slug: guardduty-describe-malware-scans-response-structure
- name: Guardduty Describe Organization Configuration Request Structure
  property_count: 0
  slug: guardduty-describe-organization-configuration-request-structure
- name: Guardduty Describe Organization Configuration Response Structure
  property_count: 6
  slug: guardduty-describe-organization-configuration-response-structure
- name: Guardduty Describe Publishing Destination Request Structure
  property_count: 0
  slug: guardduty-describe-publishing-destination-request-structure
- name: Guardduty Describe Publishing Destination Response Structure
  property_count: 5
  slug: guardduty-describe-publishing-destination-response-structure
- name: Guardduty Destination Properties Structure
  property_count: 2
  slug: guardduty-destination-properties-structure
- name: Guardduty Destination Structure
  property_count: 3
  slug: guardduty-destination-structure
- name: Guardduty Destination Type Structure
  property_count: 0
  slug: guardduty-destination-type-structure
- name: Guardduty Destinations Structure
  property_count: 0
  slug: guardduty-destinations-structure
- name: Guardduty Detector Additional Configuration Result Structure
  property_count: 3
  slug: guardduty-detector-additional-configuration-result-structure
- name: Guardduty Detector Additional Configuration Results Structure
  property_count: 0
  slug: guardduty-detector-additional-configuration-results-structure
- name: Guardduty Detector Additional Configuration Structure
  property_count: 2
  slug: guardduty-detector-additional-configuration-structure
- name: Guardduty Detector Additional Configurations Structure
  property_count: 0
  slug: guardduty-detector-additional-configurations-structure
- name: Guardduty Detector Feature Configuration Result Structure
  property_count: 4
  slug: guardduty-detector-feature-configuration-result-structure
- name: Guardduty Detector Feature Configuration Structure
  property_count: 3
  slug: guardduty-detector-feature-configuration-structure
- name: Guardduty Detector Feature Configurations Results Structure
  property_count: 0
  slug: guardduty-detector-feature-configurations-results-structure
- name: Guardduty Detector Feature Configurations Structure
  property_count: 0
  slug: guardduty-detector-feature-configurations-structure
- name: Guardduty Detector Feature Result Structure
  property_count: 0
  slug: guardduty-detector-feature-result-structure
- name: Guardduty Detector Feature Structure
  property_count: 0
  slug: guardduty-detector-feature-structure
- name: Guardduty Detector Id Structure
  property_count: 0
  slug: guardduty-detector-id-structure
- name: Guardduty Detector Ids Structure
  property_count: 0
  slug: guardduty-detector-ids-structure
- name: Guardduty Detector Status Structure
  property_count: 0
  slug: guardduty-detector-status-structure
- name: Guardduty Disable Organization Admin Account Request Structure
  property_count: 1
  slug: guardduty-disable-organization-admin-account-request-structure
- name: Guardduty Disable Organization Admin Account Response Structure
  property_count: 0
  slug: guardduty-disable-organization-admin-account-response-structure
- name: Guardduty Disassociate From Administrator Account Request Structure
  property_count: 0
  slug: guardduty-disassociate-from-administrator-account-request-structure
- name: Guardduty Disassociate From Administrator Account Response Structure
  property_count: 0
  slug: guardduty-disassociate-from-administrator-account-response-structure
- name: Guardduty Disassociate From Master Account Request Structure
  property_count: 0
  slug: guardduty-disassociate-from-master-account-request-structure
- name: Guardduty Disassociate From Master Account Response Structure
  property_count: 0
  slug: guardduty-disassociate-from-master-account-response-structure
- name: Guardduty Disassociate Members Request Structure
  property_count: 1
  slug: guardduty-disassociate-members-request-structure
- name: Guardduty Disassociate Members Response Structure
  property_count: 1
  slug: guardduty-disassociate-members-response-structure
- name: Guardduty Dns Logs Configuration Result Structure
  property_count: 1
  slug: guardduty-dns-logs-configuration-result-structure
- name: Guardduty Dns Request Action Structure
  property_count: 3
  slug: guardduty-dns-request-action-structure
- name: Guardduty Domain Details Structure
  property_count: 1
  slug: guardduty-domain-details-structure
- name: Guardduty Double Structure
  property_count: 0
  slug: guardduty-double-structure
- name: Guardduty Ebs Snapshot Preservation Structure
  property_count: 0
  slug: guardduty-ebs-snapshot-preservation-structure
- name: Guardduty Ebs Volume Details Structure
  property_count: 2
  slug: guardduty-ebs-volume-details-structure
- name: Guardduty Ebs Volume Scan Details Structure
  property_count: 6
  slug: guardduty-ebs-volume-scan-details-structure
- name: Guardduty Ebs Volumes Result Structure
  property_count: 2
  slug: guardduty-ebs-volumes-result-structure
- name: Guardduty Ecs Cluster Details Structure
  property_count: 8
  slug: guardduty-ecs-cluster-details-structure
- name: Guardduty Ecs Task Details Structure
  property_count: 10
  slug: guardduty-ecs-task-details-structure
- name: Guardduty Eks Cluster Details Structure
  property_count: 6
  slug: guardduty-eks-cluster-details-structure
- name: Guardduty Email Structure
  property_count: 0
  slug: guardduty-email-structure
- name: Guardduty Enable Organization Admin Account Request Structure
  property_count: 1
  slug: guardduty-enable-organization-admin-account-request-structure
- name: Guardduty Enable Organization Admin Account Response Structure
  property_count: 0
  slug: guardduty-enable-organization-admin-account-response-structure
- name: Guardduty Eq Structure
  property_count: 0
  slug: guardduty-eq-structure
- name: Guardduty Equals Structure
  property_count: 0
  slug: guardduty-equals-structure
- name: Guardduty Evidence Structure
  property_count: 1
  slug: guardduty-evidence-structure
- name: Guardduty Feature Additional Configuration Structure
  property_count: 0
  slug: guardduty-feature-additional-configuration-structure
- name: Guardduty Feature Status Structure
  property_count: 0
  slug: guardduty-feature-status-structure
- name: Guardduty Feedback Structure
  property_count: 0
  slug: guardduty-feedback-structure
- name: Guardduty File Paths Structure
  property_count: 0
  slug: guardduty-file-paths-structure
- name: Guardduty Filter Action Structure
  property_count: 0
  slug: guardduty-filter-action-structure
- name: Guardduty Filter Condition Structure
  property_count: 3
  slug: guardduty-filter-condition-structure
- name: Guardduty Filter Criteria Structure
  property_count: 1
  slug: guardduty-filter-criteria-structure
- name: Guardduty Filter Criterion List Structure
  property_count: 0
  slug: guardduty-filter-criterion-list-structure
- name: Guardduty Filter Criterion Structure
  property_count: 2
  slug: guardduty-filter-criterion-structure
- name: Guardduty Filter Description Structure
  property_count: 0
  slug: guardduty-filter-description-structure
- name: Guardduty Filter Name Structure
  property_count: 0
  slug: guardduty-filter-name-structure
- name: Guardduty Filter Names Structure
  property_count: 0
  slug: guardduty-filter-names-structure
- name: Guardduty Filter Rank Structure
  property_count: 0
  slug: guardduty-filter-rank-structure
- name: Guardduty Finding Criteria Structure
  property_count: 1
  slug: guardduty-finding-criteria-structure
- name: Guardduty Finding Id Structure
  property_count: 0
  slug: guardduty-finding-id-structure
- name: Guardduty Finding Ids Structure
  property_count: 0
  slug: guardduty-finding-ids-structure
- name: Guardduty Finding Publishing Frequency Structure
  property_count: 0
  slug: guardduty-finding-publishing-frequency-structure
- name: Guardduty Finding Statistic Type Structure
  property_count: 0
  slug: guardduty-finding-statistic-type-structure
- name: Guardduty Finding Statistic Types Structure
  property_count: 0
  slug: guardduty-finding-statistic-types-structure
- name: Guardduty Finding Statistics Structure
  property_count: 1
  slug: guardduty-finding-statistics-structure
- name: Guardduty Finding Structure
  property_count: 15
  slug: guardduty-finding-structure
- name: Guardduty Finding Type Structure
  property_count: 0
  slug: guardduty-finding-type-structure
- name: Guardduty Finding Types Structure
  property_count: 0
  slug: guardduty-finding-types-structure
- name: Guardduty Findings Structure
  property_count: 0
  slug: guardduty-findings-structure
- name: Guardduty Flags List Structure
  property_count: 0
  slug: guardduty-flags-list-structure
- name: Guardduty Flow Logs Configuration Result Structure
  property_count: 1
  slug: guardduty-flow-logs-configuration-result-structure
- name: Guardduty Free Trial Feature Configuration Result Structure
  property_count: 2
  slug: guardduty-free-trial-feature-configuration-result-structure
- name: Guardduty Free Trial Feature Configurations Results Structure
  property_count: 0
  slug: guardduty-free-trial-feature-configurations-results-structure
- name: Guardduty Free Trial Feature Result Structure
  property_count: 0
  slug: guardduty-free-trial-feature-result-structure
- name: Guardduty Geo Location Structure
  property_count: 2
  slug: guardduty-geo-location-structure
- name: Guardduty Get Administrator Account Request Structure
  property_count: 0
  slug: guardduty-get-administrator-account-request-structure
- name: Guardduty Get Administrator Account Response Structure
  property_count: 1
  slug: guardduty-get-administrator-account-response-structure
- name: Guardduty Get Coverage Statistics Request Structure
  property_count: 2
  slug: guardduty-get-coverage-statistics-request-structure
- name: Guardduty Get Coverage Statistics Response Structure
  property_count: 1
  slug: guardduty-get-coverage-statistics-response-structure
- name: Guardduty Get Detector Request Structure
  property_count: 0
  slug: guardduty-get-detector-request-structure
- name: Guardduty Get Detector Response Structure
  property_count: 8
  slug: guardduty-get-detector-response-structure
- name: Guardduty Get Filter Request Structure
  property_count: 0
  slug: guardduty-get-filter-request-structure
- name: Guardduty Get Filter Response Structure
  property_count: 6
  slug: guardduty-get-filter-response-structure
- name: Guardduty Get Findings Request Structure
  property_count: 2
  slug: guardduty-get-findings-request-structure
- name: Guardduty Get Findings Response Structure
  property_count: 1
  slug: guardduty-get-findings-response-structure
- name: Guardduty Get Findings Statistics Request Structure
  property_count: 2
  slug: guardduty-get-findings-statistics-request-structure
- name: Guardduty Get Findings Statistics Response Structure
  property_count: 1
  slug: guardduty-get-findings-statistics-response-structure
- name: Guardduty Get Invitations Count Request Structure
  property_count: 0
  slug: guardduty-get-invitations-count-request-structure
- name: Guardduty Get Invitations Count Response Structure
  property_count: 1
  slug: guardduty-get-invitations-count-response-structure
- name: Guardduty Get Ip Set Request Structure
  property_count: 0
  slug: guardduty-get-ip-set-request-structure
- name: Guardduty Get Ip Set Response Structure
  property_count: 5
  slug: guardduty-get-ip-set-response-structure
- name: Guardduty Get Malware Scan Settings Request Structure
  property_count: 0
  slug: guardduty-get-malware-scan-settings-request-structure
- name: Guardduty Get Malware Scan Settings Response Structure
  property_count: 2
  slug: guardduty-get-malware-scan-settings-response-structure
- name: Guardduty Get Master Account Request Structure
  property_count: 0
  slug: guardduty-get-master-account-request-structure
- name: Guardduty Get Master Account Response Structure
  property_count: 1
  slug: guardduty-get-master-account-response-structure
- name: Guardduty Get Member Detectors Request Structure
  property_count: 1
  slug: guardduty-get-member-detectors-request-structure
- name: Guardduty Get Member Detectors Response Structure
  property_count: 2
  slug: guardduty-get-member-detectors-response-structure
- name: Guardduty Get Members Request Structure
  property_count: 1
  slug: guardduty-get-members-request-structure
- name: Guardduty Get Members Response Structure
  property_count: 2
  slug: guardduty-get-members-response-structure
- name: Guardduty Get Remaining Free Trial Days Request Structure
  property_count: 1
  slug: guardduty-get-remaining-free-trial-days-request-structure
- name: Guardduty Get Remaining Free Trial Days Response Structure
  property_count: 2
  slug: guardduty-get-remaining-free-trial-days-response-structure
- name: Guardduty Get Threat Intel Set Request Structure
  property_count: 0
  slug: guardduty-get-threat-intel-set-request-structure
- name: Guardduty Get Threat Intel Set Response Structure
  property_count: 5
  slug: guardduty-get-threat-intel-set-response-structure
- name: Guardduty Get Usage Statistics Request Structure
  property_count: 5
  slug: guardduty-get-usage-statistics-request-structure
- name: Guardduty Get Usage Statistics Response Structure
  property_count: 2
  slug: guardduty-get-usage-statistics-response-structure
- name: Guardduty Groups Structure
  property_count: 0
  slug: guardduty-groups-structure
- name: Guardduty Guard Duty Arn Structure
  property_count: 0
  slug: guardduty-guard-duty-arn-structure
- name: Guardduty Highest Severity Threat Details Structure
  property_count: 3
  slug: guardduty-highest-severity-threat-details-structure
- name: Guardduty Host Path Structure
  property_count: 1
  slug: guardduty-host-path-structure
- name: Guardduty Iam Instance Profile Structure
  property_count: 2
  slug: guardduty-iam-instance-profile-structure
- name: Guardduty Instance Arn Structure
  property_count: 0
  slug: guardduty-instance-arn-structure
- name: Guardduty Instance Details Structure
  property_count: 13
  slug: guardduty-instance-details-structure
- name: Guardduty Integer Structure
  property_count: 0
  slug: guardduty-integer-structure
- name: Guardduty Integer Value With Max Structure
  property_count: 0
  slug: guardduty-integer-value-with-max-structure
- name: Guardduty Internal Server Error Exception Structure
  property_count: 0
  slug: guardduty-internal-server-error-exception-structure
- name: Guardduty Invitation Structure
  property_count: 4
  slug: guardduty-invitation-structure
- name: Guardduty Invitations Structure
  property_count: 0
  slug: guardduty-invitations-structure
- name: Guardduty Invite Members Request Structure
  property_count: 3
  slug: guardduty-invite-members-request-structure
- name: Guardduty Invite Members Response Structure
  property_count: 1
  slug: guardduty-invite-members-response-structure
- name: Guardduty Ip Set Format Structure
  property_count: 0
  slug: guardduty-ip-set-format-structure
- name: Guardduty Ip Set Ids Structure
  property_count: 0
  slug: guardduty-ip-set-ids-structure
- name: Guardduty Ip Set Status Structure
  property_count: 0
  slug: guardduty-ip-set-status-structure
- name: Guardduty Ipv6 Addresses Structure
  property_count: 0
  slug: guardduty-ipv6-addresses-structure
- name: Guardduty Kubernetes Api Call Action Structure
  property_count: 7
  slug: guardduty-kubernetes-api-call-action-structure
- name: Guardduty Kubernetes Audit Logs Configuration Result Structure
  property_count: 1
  slug: guardduty-kubernetes-audit-logs-configuration-result-structure
- name: Guardduty Kubernetes Audit Logs Configuration Structure
  property_count: 1
  slug: guardduty-kubernetes-audit-logs-configuration-structure
- name: Guardduty Kubernetes Configuration Result Structure
  property_count: 1
  slug: guardduty-kubernetes-configuration-result-structure
- name: Guardduty Kubernetes Configuration Structure
  property_count: 1
  slug: guardduty-kubernetes-configuration-structure
- name: Guardduty Kubernetes Data Source Free Trial Structure
  property_count: 1
  slug: guardduty-kubernetes-data-source-free-trial-structure
- name: Guardduty Kubernetes Details Structure
  property_count: 2
  slug: guardduty-kubernetes-details-structure
- name: Guardduty Kubernetes User Details Structure
  property_count: 3
  slug: guardduty-kubernetes-user-details-structure
- name: Guardduty Kubernetes Workload Details Structure
  property_count: 7
  slug: guardduty-kubernetes-workload-details-structure
- name: Guardduty Lambda Details Structure
  property_count: 9
  slug: guardduty-lambda-details-structure
- name: Guardduty Lineage Object Structure
  property_count: 9
  slug: guardduty-lineage-object-structure
- name: Guardduty Lineage Structure
  property_count: 0
  slug: guardduty-lineage-structure
- name: Guardduty List Coverage Request Structure
  property_count: 4
  slug: guardduty-list-coverage-request-structure
- name: Guardduty List Coverage Response Structure
  property_count: 2
  slug: guardduty-list-coverage-response-structure
- name: Guardduty List Detectors Request Structure
  property_count: 0
  slug: guardduty-list-detectors-request-structure
- name: Guardduty List Detectors Response Structure
  property_count: 2
  slug: guardduty-list-detectors-response-structure
- name: Guardduty List Filters Request Structure
  property_count: 0
  slug: guardduty-list-filters-request-structure
- name: Guardduty List Filters Response Structure
  property_count: 2
  slug: guardduty-list-filters-response-structure
- name: Guardduty List Findings Request Structure
  property_count: 4
  slug: guardduty-list-findings-request-structure
- name: Guardduty List Findings Response Structure
  property_count: 2
  slug: guardduty-list-findings-response-structure
- name: Guardduty List Invitations Request Structure
  property_count: 0
  slug: guardduty-list-invitations-request-structure
- name: Guardduty List Invitations Response Structure
  property_count: 2
  slug: guardduty-list-invitations-response-structure
- name: Guardduty List Ip Sets Request Structure
  property_count: 0
  slug: guardduty-list-ip-sets-request-structure
- name: Guardduty List Ip Sets Response Structure
  property_count: 2
  slug: guardduty-list-ip-sets-response-structure
- name: Guardduty List Members Request Structure
  property_count: 0
  slug: guardduty-list-members-request-structure
- name: Guardduty List Members Response Structure
  property_count: 2
  slug: guardduty-list-members-response-structure
- name: Guardduty List Organization Admin Accounts Request Structure
  property_count: 0
  slug: guardduty-list-organization-admin-accounts-request-structure
- name: Guardduty List Organization Admin Accounts Response Structure
  property_count: 2
  slug: guardduty-list-organization-admin-accounts-response-structure
- name: Guardduty List Publishing Destinations Request Structure
  property_count: 0
  slug: guardduty-list-publishing-destinations-request-structure
- name: Guardduty List Publishing Destinations Response Structure
  property_count: 2
  slug: guardduty-list-publishing-destinations-response-structure
- name: Guardduty List Tags For Resource Request Structure
  property_count: 0
  slug: guardduty-list-tags-for-resource-request-structure
- name: Guardduty List Tags For Resource Response Structure
  property_count: 1
  slug: guardduty-list-tags-for-resource-response-structure
- name: Guardduty List Threat Intel Sets Request Structure
  property_count: 0
  slug: guardduty-list-threat-intel-sets-request-structure
- name: Guardduty List Threat Intel Sets Response Structure
  property_count: 2
  slug: guardduty-list-threat-intel-sets-response-structure
- name: Guardduty Local Ip Details Structure
  property_count: 1
  slug: guardduty-local-ip-details-structure
- name: Guardduty Local Port Details Structure
  property_count: 2
  slug: guardduty-local-port-details-structure
- name: Guardduty Location Structure
  property_count: 0
  slug: guardduty-location-structure
- name: Guardduty Login Attribute Structure
  property_count: 4
  slug: guardduty-login-attribute-structure
- name: Guardduty Login Attributes Structure
  property_count: 0
  slug: guardduty-login-attributes-structure
- name: Guardduty Long Structure
  property_count: 0
  slug: guardduty-long-structure
- name: Guardduty Long Value Structure
  property_count: 0
  slug: guardduty-long-value-structure
- name: Guardduty Malware Protection Configuration Result Structure
  property_count: 2
  slug: guardduty-malware-protection-configuration-result-structure
- name: Guardduty Malware Protection Configuration Structure
  property_count: 1
  slug: guardduty-malware-protection-configuration-structure
- name: Guardduty Malware Protection Data Source Free Trial Structure
  property_count: 1
  slug: guardduty-malware-protection-data-source-free-trial-structure
- name: Guardduty Map Equals Structure
  property_count: 0
  slug: guardduty-map-equals-structure
- name: Guardduty Master Structure
  property_count: 4
  slug: guardduty-master-structure
- name: Guardduty Max Results Structure
  property_count: 0
  slug: guardduty-max-results-structure
- name: Guardduty Member Additional Configuration Result Structure
  property_count: 3
  slug: guardduty-member-additional-configuration-result-structure
- name: Guardduty Member Additional Configuration Results Structure
  property_count: 0
  slug: guardduty-member-additional-configuration-results-structure
- name: Guardduty Member Additional Configuration Structure
  property_count: 2
  slug: guardduty-member-additional-configuration-structure
- name: Guardduty Member Additional Configurations Structure
  property_count: 0
  slug: guardduty-member-additional-configurations-structure
- name: Guardduty Member Data Source Configuration Structure
  property_count: 3
  slug: guardduty-member-data-source-configuration-structure
- name: Guardduty Member Data Source Configurations Structure
  property_count: 0
  slug: guardduty-member-data-source-configurations-structure
- name: Guardduty Member Features Configuration Result Structure
  property_count: 4
  slug: guardduty-member-features-configuration-result-structure
- name: Guardduty Member Features Configuration Structure
  property_count: 3
  slug: guardduty-member-features-configuration-structure
- name: Guardduty Member Features Configurations Results Structure
  property_count: 0
  slug: guardduty-member-features-configurations-results-structure
- name: Guardduty Member Features Configurations Structure
  property_count: 0
  slug: guardduty-member-features-configurations-structure
- name: Guardduty Member Structure
  property_count: 8
  slug: guardduty-member-structure
- name: Guardduty Members Structure
  property_count: 0
  slug: guardduty-members-structure
- name: Guardduty Memory Regions List Structure
  property_count: 0
  slug: guardduty-memory-regions-list-structure
- name: Guardduty Name Structure
  property_count: 0
  slug: guardduty-name-structure
- name: Guardduty Neq Structure
  property_count: 0
  slug: guardduty-neq-structure
- name: Guardduty Network Connection Action Structure
  property_count: 7
  slug: guardduty-network-connection-action-structure
- name: Guardduty Network Interface Structure
  property_count: 10
  slug: guardduty-network-interface-structure
- name: Guardduty Network Interfaces Structure
  property_count: 0
  slug: guardduty-network-interfaces-structure
- name: Guardduty Non Empty String Structure
  property_count: 0
  slug: guardduty-non-empty-string-structure
- name: Guardduty Not Equals Structure
  property_count: 0
  slug: guardduty-not-equals-structure
- name: Guardduty Order By Structure
  property_count: 0
  slug: guardduty-order-by-structure
- name: Guardduty Org Feature Additional Configuration Structure
  property_count: 0
  slug: guardduty-org-feature-additional-configuration-structure
- name: Guardduty Org Feature Status Structure
  property_count: 0
  slug: guardduty-org-feature-status-structure
- name: Guardduty Org Feature Structure
  property_count: 0
  slug: guardduty-org-feature-structure
- name: Guardduty Organization Additional Configuration Result Structure
  property_count: 2
  slug: guardduty-organization-additional-configuration-result-structure
- name: Guardduty Organization Additional Configuration Results Structure
  property_count: 0
  slug: guardduty-organization-additional-configuration-results-structure
- name: Guardduty Organization Additional Configuration Structure
  property_count: 2
  slug: guardduty-organization-additional-configuration-structure
- name: Guardduty Organization Additional Configurations Structure
  property_count: 0
  slug: guardduty-organization-additional-configurations-structure
- name: Guardduty Organization Data Source Configurations Result Structure
  property_count: 3
  slug: guardduty-organization-data-source-configurations-result-structure
- name: Guardduty Organization Data Source Configurations Structure
  property_count: 3
  slug: guardduty-organization-data-source-configurations-structure
- name: Guardduty Organization Ebs Volumes Result Structure
  property_count: 1
  slug: guardduty-organization-ebs-volumes-result-structure
- name: Guardduty Organization Ebs Volumes Structure
  property_count: 1
  slug: guardduty-organization-ebs-volumes-structure
- name: Guardduty Organization Feature Configuration Result Structure
  property_count: 3
  slug: guardduty-organization-feature-configuration-result-structure
- name: Guardduty Organization Feature Configuration Structure
  property_count: 3
  slug: guardduty-organization-feature-configuration-structure
- name: Guardduty Organization Features Configurations Results Structure
  property_count: 0
  slug: guardduty-organization-features-configurations-results-structure
- name: Guardduty Organization Features Configurations Structure
  property_count: 0
  slug: guardduty-organization-features-configurations-structure
- name: Guardduty Organization Kubernetes Audit Logs Configuration Result Structure
  property_count: 1
  slug: guardduty-organization-kubernetes-audit-logs-configuration-result-structure
- name: Guardduty Organization Kubernetes Audit Logs Configuration Structure
  property_count: 1
  slug: guardduty-organization-kubernetes-audit-logs-configuration-structure
- name: Guardduty Organization Kubernetes Configuration Result Structure
  property_count: 1
  slug: guardduty-organization-kubernetes-configuration-result-structure
- name: Guardduty Organization Kubernetes Configuration Structure
  property_count: 1
  slug: guardduty-organization-kubernetes-configuration-structure
- name: Guardduty Organization Malware Protection Configuration Result Structure
  property_count: 1
  slug: guardduty-organization-malware-protection-configuration-result-structure
- name: Guardduty Organization Malware Protection Configuration Structure
  property_count: 1
  slug: guardduty-organization-malware-protection-configuration-structure
- name: Guardduty Organization S3 Logs Configuration Result Structure
  property_count: 1
  slug: guardduty-organization-s3-logs-configuration-result-structure
- name: Guardduty Organization S3 Logs Configuration Structure
  property_count: 1
  slug: guardduty-organization-s3-logs-configuration-structure
- name: Guardduty Organization Scan Ec2 Instance With Findings Result Structure
  property_count: 1
  slug: guardduty-organization-scan-ec2-instance-with-findings-result-structure
- name: Guardduty Organization Scan Ec2 Instance With Findings Structure
  property_count: 1
  slug: guardduty-organization-scan-ec2-instance-with-findings-structure
- name: Guardduty Organization Structure
  property_count: 4
  slug: guardduty-organization-structure
- name: Guardduty Owner Structure
  property_count: 1
  slug: guardduty-owner-structure
- name: Guardduty Permission Configuration Structure
  property_count: 2
  slug: guardduty-permission-configuration-structure
- name: Guardduty Port Probe Action Structure
  property_count: 2
  slug: guardduty-port-probe-action-structure
- name: Guardduty Port Probe Detail Structure
  property_count: 3
  slug: guardduty-port-probe-detail-structure
- name: Guardduty Port Probe Details Structure
  property_count: 0
  slug: guardduty-port-probe-details-structure
- name: Guardduty Positive Long Structure
  property_count: 0
  slug: guardduty-positive-long-structure
- name: Guardduty Private Ip Address Details Structure
  property_count: 2
  slug: guardduty-private-ip-address-details-structure
- name: Guardduty Private Ip Addresses Structure
  property_count: 0
  slug: guardduty-private-ip-addresses-structure
- name: Guardduty Process Details Structure
  property_count: 13
  slug: guardduty-process-details-structure
- name: Guardduty Product Code Structure
  property_count: 2
  slug: guardduty-product-code-structure
- name: Guardduty Product Codes Structure
  property_count: 0
  slug: guardduty-product-codes-structure
- name: Guardduty Public Access Structure
  property_count: 2
  slug: guardduty-public-access-structure
- name: Guardduty Publishing Status Structure
  property_count: 0
  slug: guardduty-publishing-status-structure
- name: Guardduty Rds Db Instance Details Structure
  property_count: 6
  slug: guardduty-rds-db-instance-details-structure
- name: Guardduty Rds Db User Details Structure
  property_count: 5
  slug: guardduty-rds-db-user-details-structure
- name: Guardduty Rds Login Attempt Action Structure
  property_count: 2
  slug: guardduty-rds-login-attempt-action-structure
- name: Guardduty Remote Account Details Structure
  property_count: 2
  slug: guardduty-remote-account-details-structure
- name: Guardduty Remote Ip Details Structure
  property_count: 5
  slug: guardduty-remote-ip-details-structure
- name: Guardduty Remote Port Details Structure
  property_count: 2
  slug: guardduty-remote-port-details-structure
- name: Guardduty Resource Details Structure
  property_count: 1
  slug: guardduty-resource-details-structure
- name: Guardduty Resource List Structure
  property_count: 0
  slug: guardduty-resource-list-structure
- name: Guardduty Resource Structure
  property_count: 12
  slug: guardduty-resource-structure
- name: Guardduty Resource Type Structure
  property_count: 0
  slug: guardduty-resource-type-structure
- name: Guardduty Runtime Context Structure
  property_count: 20
  slug: guardduty-runtime-context-structure
- name: Guardduty Runtime Details Structure
  property_count: 2
  slug: guardduty-runtime-details-structure
- name: Guardduty S3 Bucket Detail Structure
  property_count: 8
  slug: guardduty-s3-bucket-detail-structure
- name: Guardduty S3 Bucket Details Structure
  property_count: 0
  slug: guardduty-s3-bucket-details-structure
- name: Guardduty S3 Logs Configuration Result Structure
  property_count: 1
  slug: guardduty-s3-logs-configuration-result-structure
- name: Guardduty S3 Logs Configuration Structure
  property_count: 1
  slug: guardduty-s3-logs-configuration-structure
- name: Guardduty Scan Condition Pair Structure
  property_count: 2
  slug: guardduty-scan-condition-pair-structure
- name: Guardduty Scan Condition Structure
  property_count: 1
  slug: guardduty-scan-condition-structure
- name: Guardduty Scan Criterion Key Structure
  property_count: 0
  slug: guardduty-scan-criterion-key-structure
- name: Guardduty Scan Criterion Structure
  property_count: 0
  slug: guardduty-scan-criterion-structure
- name: Guardduty Scan Detections Structure
  property_count: 4
  slug: guardduty-scan-detections-structure
- name: Guardduty Scan Ec2 Instance With Findings Result Structure
  property_count: 1
  slug: guardduty-scan-ec2-instance-with-findings-result-structure
- name: Guardduty Scan Ec2 Instance With Findings Structure
  property_count: 1
  slug: guardduty-scan-ec2-instance-with-findings-structure
- name: Guardduty Scan File Path Structure
  property_count: 4
  slug: guardduty-scan-file-path-structure
- name: Guardduty Scan Resource Criteria Structure
  property_count: 2
  slug: guardduty-scan-resource-criteria-structure
- name: Guardduty Scan Result Details Structure
  property_count: 1
  slug: guardduty-scan-result-details-structure
- name: Guardduty Scan Result Structure
  property_count: 0
  slug: guardduty-scan-result-structure
- name: Guardduty Scan Status Structure
  property_count: 0
  slug: guardduty-scan-status-structure
- name: Guardduty Scan Structure
  property_count: 14
  slug: guardduty-scan-structure
- name: Guardduty Scan Threat Name Structure
  property_count: 4
  slug: guardduty-scan-threat-name-structure
- name: Guardduty Scan Threat Names Structure
  property_count: 0
  slug: guardduty-scan-threat-names-structure
- name: Guardduty Scanned Item Count Structure
  property_count: 3
  slug: guardduty-scanned-item-count-structure
- name: Guardduty Scans Structure
  property_count: 0
  slug: guardduty-scans-structure
- name: Guardduty Security Context Structure
  property_count: 1
  slug: guardduty-security-context-structure
- name: Guardduty Security Group Structure
  property_count: 2
  slug: guardduty-security-group-structure
- name: Guardduty Security Groups Structure
  property_count: 0
  slug: guardduty-security-groups-structure
- name: Guardduty Service Additional Info Structure
  property_count: 2
  slug: guardduty-service-additional-info-structure
- name: Guardduty Service Structure
  property_count: 14
  slug: guardduty-service-structure
- name: Guardduty Sort Criteria Structure
  property_count: 2
  slug: guardduty-sort-criteria-structure
- name: Guardduty Source Ips Structure
  property_count: 0
  slug: guardduty-source-ips-structure
- name: Guardduty Sources Structure
  property_count: 0
  slug: guardduty-sources-structure
- name: Guardduty Start Monitoring Members Request Structure
  property_count: 1
  slug: guardduty-start-monitoring-members-request-structure
- name: Guardduty Start Monitoring Members Response Structure
  property_count: 1
  slug: guardduty-start-monitoring-members-response-structure
- name: Guardduty Stop Monitoring Members Request Structure
  property_count: 1
  slug: guardduty-stop-monitoring-members-request-structure
- name: Guardduty Stop Monitoring Members Response Structure
  property_count: 1
  slug: guardduty-stop-monitoring-members-response-structure
- name: Guardduty String Structure
  property_count: 0
  slug: guardduty-string-structure
- name: Guardduty Subnet Ids Structure
  property_count: 0
  slug: guardduty-subnet-ids-structure
- name: Guardduty Tag Key List Structure
  property_count: 0
  slug: guardduty-tag-key-list-structure
- name: Guardduty Tag Key Structure
  property_count: 0
  slug: guardduty-tag-key-structure
- name: Guardduty Tag Map Structure
  property_count: 0
  slug: guardduty-tag-map-structure
- name: Guardduty Tag Resource Request Structure
  property_count: 1
  slug: guardduty-tag-resource-request-structure
- name: Guardduty Tag Resource Response Structure
  property_count: 0
  slug: guardduty-tag-resource-response-structure
- name: Guardduty Tag Structure
  property_count: 2
  slug: guardduty-tag-structure
- name: Guardduty Tag Value Structure
  property_count: 0
  slug: guardduty-tag-value-structure
- name: Guardduty Tags Structure
  property_count: 0
  slug: guardduty-tags-structure
- name: Guardduty Threat Detected By Name Structure
  property_count: 4
  slug: guardduty-threat-detected-by-name-structure
- name: Guardduty Threat Intel Set Format Structure
  property_count: 0
  slug: guardduty-threat-intel-set-format-structure
- name: Guardduty Threat Intel Set Ids Structure
  property_count: 0
  slug: guardduty-threat-intel-set-ids-structure
- name: Guardduty Threat Intel Set Status Structure
  property_count: 0
  slug: guardduty-threat-intel-set-status-structure
- name: Guardduty Threat Intelligence Detail Structure
  property_count: 2
  slug: guardduty-threat-intelligence-detail-structure
- name: Guardduty Threat Intelligence Details Structure
  property_count: 0
  slug: guardduty-threat-intelligence-details-structure
- name: Guardduty Threat Names Structure
  property_count: 0
  slug: guardduty-threat-names-structure
- name: Guardduty Threats Detected Item Count Structure
  property_count: 1
  slug: guardduty-threats-detected-item-count-structure
- name: Guardduty Timestamp Structure
  property_count: 0
  slug: guardduty-timestamp-structure
- name: Guardduty Total Structure
  property_count: 2
  slug: guardduty-total-structure
- name: Guardduty Trigger Details Structure
  property_count: 2
  slug: guardduty-trigger-details-structure
- name: Guardduty Unarchive Findings Request Structure
  property_count: 1
  slug: guardduty-unarchive-findings-request-structure
- name: Guardduty Unarchive Findings Response Structure
  property_count: 0
  slug: guardduty-unarchive-findings-response-structure
- name: Guardduty Unprocessed Account Structure
  property_count: 2
  slug: guardduty-unprocessed-account-structure
- name: Guardduty Unprocessed Accounts Structure
  property_count: 0
  slug: guardduty-unprocessed-accounts-structure
- name: Guardduty Unprocessed Data Sources Result Structure
  property_count: 1
  slug: guardduty-unprocessed-data-sources-result-structure
- name: Guardduty Untag Resource Request Structure
  property_count: 0
  slug: guardduty-untag-resource-request-structure
- name: Guardduty Untag Resource Response Structure
  property_count: 0
  slug: guardduty-untag-resource-response-structure
- name: Guardduty Update Detector Request Structure
  property_count: 4
  slug: guardduty-update-detector-request-structure
- name: Guardduty Update Detector Response Structure
  property_count: 0
  slug: guardduty-update-detector-response-structure
- name: Guardduty Update Filter Request Structure
  property_count: 4
  slug: guardduty-update-filter-request-structure
- name: Guardduty Update Filter Response Structure
  property_count: 1
  slug: guardduty-update-filter-response-structure
- name: Guardduty Update Findings Feedback Request Structure
  property_count: 3
  slug: guardduty-update-findings-feedback-request-structure
- name: Guardduty Update Findings Feedback Response Structure
  property_count: 0
  slug: guardduty-update-findings-feedback-response-structure
- name: Guardduty Update Ip Set Request Structure
  property_count: 3
  slug: guardduty-update-ip-set-request-structure
- name: Guardduty Update Ip Set Response Structure
  property_count: 0
  slug: guardduty-update-ip-set-response-structure
- name: Guardduty Update Malware Scan Settings Request Structure
  property_count: 2
  slug: guardduty-update-malware-scan-settings-request-structure
- name: Guardduty Update Malware Scan Settings Response Structure
  property_count: 0
  slug: guardduty-update-malware-scan-settings-response-structure
- name: Guardduty Update Member Detectors Request Structure
  property_count: 3
  slug: guardduty-update-member-detectors-request-structure
- name: Guardduty Update Member Detectors Response Structure
  property_count: 1
  slug: guardduty-update-member-detectors-response-structure
- name: Guardduty Update Organization Configuration Request Structure
  property_count: 4
  slug: guardduty-update-organization-configuration-request-structure
- name: Guardduty Update Organization Configuration Response Structure
  property_count: 0
  slug: guardduty-update-organization-configuration-response-structure
- name: Guardduty Update Publishing Destination Request Structure
  property_count: 1
  slug: guardduty-update-publishing-destination-request-structure
- name: Guardduty Update Publishing Destination Response Structure
  property_count: 0
  slug: guardduty-update-publishing-destination-response-structure
- name: Guardduty Update Threat Intel Set Request Structure
  property_count: 3
  slug: guardduty-update-threat-intel-set-request-structure
- name: Guardduty Update Threat Intel Set Response Structure
  property_count: 0
  slug: guardduty-update-threat-intel-set-response-structure
- name: Guardduty Usage Account Result List Structure
  property_count: 0
  slug: guardduty-usage-account-result-list-structure
- name: Guardduty Usage Account Result Structure
  property_count: 2
  slug: guardduty-usage-account-result-structure
- name: Guardduty Usage Criteria Structure
  property_count: 4
  slug: guardduty-usage-criteria-structure
- name: Guardduty Usage Data Source Result List Structure
  property_count: 0
  slug: guardduty-usage-data-source-result-list-structure
- name: Guardduty Usage Data Source Result Structure
  property_count: 2
  slug: guardduty-usage-data-source-result-structure
- name: Guardduty Usage Feature List Structure
  property_count: 0
  slug: guardduty-usage-feature-list-structure
- name: Guardduty Usage Feature Result List Structure
  property_count: 0
  slug: guardduty-usage-feature-result-list-structure
- name: Guardduty Usage Feature Result Structure
  property_count: 2
  slug: guardduty-usage-feature-result-structure
- name: Guardduty Usage Feature Structure
  property_count: 0
  slug: guardduty-usage-feature-structure
- name: Guardduty Usage Resource Result List Structure
  property_count: 0
  slug: guardduty-usage-resource-result-list-structure
- name: Guardduty Usage Resource Result Structure
  property_count: 2
  slug: guardduty-usage-resource-result-structure
- name: Guardduty Usage Statistic Type Structure
  property_count: 0
  slug: guardduty-usage-statistic-type-structure
- name: Guardduty Usage Statistics Structure
  property_count: 5
  slug: guardduty-usage-statistics-structure
- name: Guardduty Volume Detail Structure
  property_count: 7
  slug: guardduty-volume-detail-structure
- name: Guardduty Volume Details Structure
  property_count: 0
  slug: guardduty-volume-details-structure
- name: Guardduty Volume Mount Structure
  property_count: 2
  slug: guardduty-volume-mount-structure
- name: Guardduty Volume Mounts Structure
  property_count: 0
  slug: guardduty-volume-mounts-structure
- name: Guardduty Volume Structure
  property_count: 2
  slug: guardduty-volume-structure
- name: Guardduty Volumes Structure
  property_count: 0
  slug: guardduty-volumes-structure
- name: Guardduty Vpc Config Structure
  property_count: 3
  slug: guardduty-vpc-config-structure
jsonld:
- class_count: 247
  name: Amazon Guardduty Context
  property_count: 297
  slug: amazon-guardduty-context
layout: provider
modified: '2026-05-19'
name: Amazon GuardDuty
nav: Providers
network: true
overview: 'Amazon GuardDuty publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Detector API, Invitation API, and 1 more. Tagged areas include Anomaly Detection, Compliance, Machine-Learning, Monitoring, and Security.


  The Amazon GuardDuty catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon GuardDuty''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 12 more developer resources.'
plans:
- name: Amazon Guardduty Plans Pricing
  plan_count: 3
  slug: amazon-guardduty-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Amazon Guardduty Rate Limits
  slug: amazon-guardduty-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon GuardDuty API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-guardduty-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Amazon GuardDuty API Rules
  rule_count: 16
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 9
  slug: amazon-guardduty-spectral-rules
score:
  band: developing
  composite: 53.5
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 17.4
    contract_quality: 76.2
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 17.4
    operational_transparency: 26.3
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-guardduty/refs/heads/main/screenshots/amazon-guardduty-2026-06-20T171659.png
security:
- kind: authentication
  name: Amazon Guardduty Authentication
  slug: amazon-guardduty-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Guardduty Domain Security
  slug: amazon-guardduty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Guardduty Vulnerability Disclosure
  slug: amazon-guardduty-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Guardduty Trust Center
  slug: amazon-guardduty-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-guardduty
tags:
- Anomaly Detection
- Compliance
- Machine-Learning
- Monitoring
- Security
- Threat Detection
use_cases:
- description: Detect compromised AWS credentials and unauthorized API calls using ML-based anomaly detection.
  name: Account Compromise Detection
- description: Identify suspicious behavior from privileged users or compromised internal accounts.
  name: Insider Threat Monitoring
- description: Detect and alert on unauthorized cryptocurrency mining using EC2 or Lambda resources.
  name: Cryptocurrency Mining Detection
- description: Scan workloads and data for malware and ransomware threats.
  name: Malware Detection
- description: Identify unusual data access patterns and potential exfiltration from S3 buckets.
  name: Data Exfiltration Prevention
website: https://aws.amazon.com/guardduty/
---
