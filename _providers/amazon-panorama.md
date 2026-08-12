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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Amazon Panorama Agentic Access
  operation_count: 34
  slug: amazon-panorama-agentic-access
  summary_line: 34 operations · 15 acting
api_count: 6
apis:
- description: The Application Instances API from Amazon Panorama — 6 operation(s) for application instances.
  name: Amazon Panorama Application Instances API
  slug: amazon-panorama-application-instances-api
- description: The Devices API from Amazon Panorama — 2 operation(s) for devices.
  name: Amazon Panorama Devices API
  slug: amazon-panorama-devices-api
- description: The Jobs API from Amazon Panorama — 2 operation(s) for jobs.
  name: Amazon Panorama Jobs API
  slug: amazon-panorama-jobs-api
- description: The Nodes API from Amazon Panorama — 2 operation(s) for nodes.
  name: Amazon Panorama Nodes API
  slug: amazon-panorama-nodes-api
- description: The Packages API from Amazon Panorama — 9 operation(s) for packages.
  name: Amazon Panorama Packages API
  slug: amazon-panorama-packages-api
- description: The Tags API from Amazon Panorama — 2 operation(s) for tags.
  name: Amazon Panorama Tags API
  slug: amazon-panorama-tags-api
artifact_total: 687
collections:
- collection_type: postman
  name: AWS Panorama Application Instances API
  slug: postman-amazon-panorama-application-instances-api
- collection_type: postman
  name: AWS Panorama Application Instances Devices API
  slug: postman-amazon-panorama-devices-api
- collection_type: postman
  name: AWS Panorama Application Instances Jobs API
  slug: postman-amazon-panorama-jobs-api
- collection_type: postman
  name: AWS Panorama Application Instances Nodes API
  slug: postman-amazon-panorama-nodes-api
- collection_type: postman
  name: AWS Panorama Application Instances Packages API
  slug: postman-amazon-panorama-packages-api
- collection_type: postman
  name: AWS Panorama Application Instances Tags API
  slug: postman-amazon-panorama-tags-api
- collection_type: open
  name: AWS Panorama
  slug: open-amazon-panorama
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-panorama/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-panorama-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-panorama-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-panorama-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-panorama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-panorama-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/panorama/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/panorama/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/panorama/
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
  url: https://aws.amazon.com/blogs/machine-learning/tag/aws-panorama/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/panorama/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
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
  url: rules/amazon-panorama-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-panorama-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-panorama-openapi-context.jsonld
- group: docs
  title: Openapi Access Denied Exception
  type: JSONSchema
  url: json-schema/openapi-access-denied-exception-schema.json
- group: docs
  title: Openapi Alternate Software Metadata
  type: JSONSchema
  url: json-schema/openapi-alternate-software-metadata-schema.json
- group: docs
  title: Openapi Alternate Softwares
  type: JSONSchema
  url: json-schema/openapi-alternate-softwares-schema.json
- group: docs
  title: Openapi Application Instance Arn
  type: JSONSchema
  url: json-schema/openapi-application-instance-arn-schema.json
- group: docs
  title: Openapi Application Instance Health Status
  type: JSONSchema
  url: json-schema/openapi-application-instance-health-status-schema.json
created: '2026-03-16'
description: AWS Panorama is a machine learning appliance and software development kit (SDK) that brings computer vision to on-premises cameras. It allows organizations to automate visual inspection tasks, such as gauging production line efficiency or identifying bottlenecks in industrial operations.
examples:
- key_count: 0
  name: Openapi Access Denied Exception Example
  slug: openapi-access-denied-exception-example
- key_count: 1
  name: Openapi Alternate Software Metadata Example
  slug: openapi-alternate-software-metadata-example
- key_count: 0
  name: Openapi Application Instance Arn Example
  slug: openapi-application-instance-arn-example
- key_count: 12
  name: Openapi Application Instance Example
  slug: openapi-application-instance-example
- key_count: 0
  name: Openapi Application Instance Health Status Example
  slug: openapi-application-instance-health-status-example
- key_count: 0
  name: Openapi Application Instance Id Example
  slug: openapi-application-instance-id-example
- key_count: 0
  name: Openapi Application Instance Name Example
  slug: openapi-application-instance-name-example
- key_count: 0
  name: Openapi Application Instance Status Description Example
  slug: openapi-application-instance-status-description-example
- key_count: 0
  name: Openapi Application Instance Status Example
  slug: openapi-application-instance-status-example
- key_count: 0
  name: Openapi Boolean Example
  slug: openapi-boolean-example
- key_count: 0
  name: Openapi Bucket Example
  slug: openapi-bucket-example
- key_count: 0
  name: Openapi Bucket Name Example
  slug: openapi-bucket-name-example
- key_count: 0
  name: Openapi Certificates Example
  slug: openapi-certificates-example
- key_count: 0
  name: Openapi Client Token Example
  slug: openapi-client-token-example
- key_count: 0
  name: Openapi Conflict Exception Example
  slug: openapi-conflict-exception-example
- key_count: 0
  name: Openapi Connection Type Example
  slug: openapi-connection-type-example
- key_count: 8
  name: Openapi Create Application Instance Request Example
  slug: openapi-create-application-instance-request-example
- key_count: 1
  name: Openapi Create Application Instance Response Example
  slug: openapi-create-application-instance-response-example
- key_count: 3
  name: Openapi Create Job For Devices Request Example
  slug: openapi-create-job-for-devices-request-example
- key_count: 1
  name: Openapi Create Job For Devices Response Example
  slug: openapi-create-job-for-devices-response-example
- key_count: 7
  name: Openapi Create Node From Template Job Request Example
  slug: openapi-create-node-from-template-job-request-example
- key_count: 1
  name: Openapi Create Node From Template Job Response Example
  slug: openapi-create-node-from-template-job-response-example
- key_count: 5
  name: Openapi Create Package Import Job Request Example
  slug: openapi-create-package-import-job-request-example
- key_count: 1
  name: Openapi Create Package Import Job Response Example
  slug: openapi-create-package-import-job-response-example
- key_count: 2
  name: Openapi Create Package Request Example
  slug: openapi-create-package-request-example
- key_count: 3
  name: Openapi Create Package Response Example
  slug: openapi-create-package-response-example
- key_count: 0
  name: Openapi Created Time Example
  slug: openapi-created-time-example
- key_count: 0
  name: Openapi Current Software Example
  slug: openapi-current-software-example
- key_count: 0
  name: Openapi Default Gateway Example
  slug: openapi-default-gateway-example
- key_count: 0
  name: Openapi Default Runtime Context Device Example
  slug: openapi-default-runtime-context-device-example
- key_count: 0
  name: Openapi Delete Device Request Example
  slug: openapi-delete-device-request-example
- key_count: 1
  name: Openapi Delete Device Response Example
  slug: openapi-delete-device-response-example
- key_count: 0
  name: Openapi Delete Package Request Example
  slug: openapi-delete-package-request-example
- key_count: 0
  name: Openapi Delete Package Response Example
  slug: openapi-delete-package-response-example
- key_count: 0
  name: Openapi Deregister Package Version Request Example
  slug: openapi-deregister-package-version-request-example
- key_count: 0
  name: Openapi Deregister Package Version Response Example
  slug: openapi-deregister-package-version-response-example
- key_count: 0
  name: Openapi Describe Application Instance Details Request Example
  slug: openapi-describe-application-instance-details-request-example
- key_count: 8
  name: Openapi Describe Application Instance Details Response Example
  slug: openapi-describe-application-instance-details-response-example
- key_count: 0
  name: Openapi Describe Application Instance Request Example
  slug: openapi-describe-application-instance-request-example
- key_count: 15
  name: Openapi Describe Application Instance Response Example
  slug: openapi-describe-application-instance-response-example
- key_count: 0
  name: Openapi Describe Device Job Request Example
  slug: openapi-describe-device-job-request-example
- key_count: 9
  name: Openapi Describe Device Job Response Example
  slug: openapi-describe-device-job-response-example
- key_count: 0
  name: Openapi Describe Device Request Example
  slug: openapi-describe-device-request-example
- key_count: 15
  name: Openapi Describe Device Response Example
  slug: openapi-describe-device-response-example
- key_count: 0
  name: Openapi Describe Node From Template Job Request Example
  slug: openapi-describe-node-from-template-job-request-example
- key_count: 12
  name: Openapi Describe Node From Template Job Response Example
  slug: openapi-describe-node-from-template-job-response-example
- key_count: 0
  name: Openapi Describe Node Request Example
  slug: openapi-describe-node-request-example
- key_count: 14
  name: Openapi Describe Node Response Example
  slug: openapi-describe-node-response-example
- key_count: 0
  name: Openapi Describe Package Import Job Request Example
  slug: openapi-describe-package-import-job-request-example
- key_count: 11
  name: Openapi Describe Package Import Job Response Example
  slug: openapi-describe-package-import-job-response-example
- key_count: 0
  name: Openapi Describe Package Request Example
  slug: openapi-describe-package-request-example
- key_count: 8
  name: Openapi Describe Package Response Example
  slug: openapi-describe-package-response-example
- key_count: 0
  name: Openapi Describe Package Version Request Example
  slug: openapi-describe-package-version-request-example
- key_count: 10
  name: Openapi Describe Package Version Response Example
  slug: openapi-describe-package-version-response-example
- key_count: 0
  name: Openapi Description Example
  slug: openapi-description-example
- key_count: 0
  name: Openapi Desired State Example
  slug: openapi-desired-state-example
- key_count: 0
  name: Openapi Device Aggregated Status Example
  slug: openapi-device-aggregated-status-example
- key_count: 0
  name: Openapi Device Arn Example
  slug: openapi-device-arn-example
- key_count: 0
  name: Openapi Device Brand Example
  slug: openapi-device-brand-example
- key_count: 0
  name: Openapi Device Connection Status Example
  slug: openapi-device-connection-status-example
- key_count: 13
  name: Openapi Device Example
  slug: openapi-device-example
- key_count: 0
  name: Openapi Device Id Example
  slug: openapi-device-id-example
- key_count: 1
  name: Openapi Device Job Config Example
  slug: openapi-device-job-config-example
- key_count: 5
  name: Openapi Device Job Example
  slug: openapi-device-job-example
- key_count: 0
  name: Openapi Device Name Example
  slug: openapi-device-name-example
- key_count: 0
  name: Openapi Device Reported Status Example
  slug: openapi-device-reported-status-example
- key_count: 0
  name: Openapi Device Serial Number Example
  slug: openapi-device-serial-number-example
- key_count: 0
  name: Openapi Device Status Example
  slug: openapi-device-status-example
- key_count: 0
  name: Openapi Device Type Example
  slug: openapi-device-type-example
- key_count: 0
  name: Openapi Dns Example
  slug: openapi-dns-example
- key_count: 2
  name: Openapi Ethernet Payload Example
  slug: openapi-ethernet-payload-example
- key_count: 3
  name: Openapi Ethernet Status Example
  slug: openapi-ethernet-status-example
- key_count: 0
  name: Openapi Hw Address Example
  slug: openapi-hw-address-example
- key_count: 0
  name: Openapi Image Version Example
  slug: openapi-image-version-example
- key_count: 0
  name: Openapi Internal Server Exception Example
  slug: openapi-internal-server-exception-example
- key_count: 0
  name: Openapi Iot Thing Name Example
  slug: openapi-iot-thing-name-example
- key_count: 0
  name: Openapi Ip Address Example
  slug: openapi-ip-address-example
- key_count: 0
  name: Openapi Ip Address Or Server Name Example
  slug: openapi-ip-address-or-server-name-example
- key_count: 2
  name: Openapi Job Example
  slug: openapi-job-example
- key_count: 0
  name: Openapi Job Id Example
  slug: openapi-job-id-example
- key_count: 2
  name: Openapi Job Resource Tags Example
  slug: openapi-job-resource-tags-example
- key_count: 0
  name: Openapi Job Resource Type Example
  slug: openapi-job-resource-type-example
- key_count: 0
  name: Openapi Job Type Example
  slug: openapi-job-type-example
- key_count: 0
  name: Openapi Last Updated Time Example
  slug: openapi-last-updated-time-example
- key_count: 0
  name: Openapi Latest Alternate Software Example
  slug: openapi-latest-alternate-software-example
- key_count: 3
  name: Openapi Latest Device Job Example
  slug: openapi-latest-device-job-example
- key_count: 0
  name: Openapi Latest Software Example
  slug: openapi-latest-software-example
- key_count: 0
  name: Openapi Lease Expiration Time Example
  slug: openapi-lease-expiration-time-example
- key_count: 0
  name: Openapi List Application Instance Dependencies Request Example
  slug: openapi-list-application-instance-dependencies-request-example
- key_count: 2
  name: Openapi List Application Instance Dependencies Response Example
  slug: openapi-list-application-instance-dependencies-response-example
- key_count: 0
  name: Openapi List Application Instance Node Instances Request Example
  slug: openapi-list-application-instance-node-instances-request-example
- key_count: 2
  name: Openapi List Application Instance Node Instances Response Example
  slug: openapi-list-application-instance-node-instances-response-example
- key_count: 0
  name: Openapi List Application Instances Request Example
  slug: openapi-list-application-instances-request-example
- key_count: 2
  name: Openapi List Application Instances Response Example
  slug: openapi-list-application-instances-response-example
- key_count: 0
  name: Openapi List Devices Jobs Request Example
  slug: openapi-list-devices-jobs-request-example
- key_count: 2
  name: Openapi List Devices Jobs Response Example
  slug: openapi-list-devices-jobs-response-example
- key_count: 0
  name: Openapi List Devices Request Example
  slug: openapi-list-devices-request-example
- key_count: 2
  name: Openapi List Devices Response Example
  slug: openapi-list-devices-response-example
- key_count: 0
  name: Openapi List Devices Sort By Example
  slug: openapi-list-devices-sort-by-example
- key_count: 0
  name: Openapi List Node From Template Jobs Request Example
  slug: openapi-list-node-from-template-jobs-request-example
- key_count: 2
  name: Openapi List Node From Template Jobs Response Example
  slug: openapi-list-node-from-template-jobs-response-example
- key_count: 0
  name: Openapi List Nodes Request Example
  slug: openapi-list-nodes-request-example
- key_count: 2
  name: Openapi List Nodes Response Example
  slug: openapi-list-nodes-response-example
- key_count: 0
  name: Openapi List Package Import Jobs Request Example
  slug: openapi-list-package-import-jobs-request-example
- key_count: 2
  name: Openapi List Package Import Jobs Response Example
  slug: openapi-list-package-import-jobs-response-example
- key_count: 0
  name: Openapi List Packages Request Example
  slug: openapi-list-packages-request-example
- key_count: 2
  name: Openapi List Packages Response Example
  slug: openapi-list-packages-response-example
- key_count: 0
  name: Openapi List Tags For Resource Request Example
  slug: openapi-list-tags-for-resource-request-example
- key_count: 1
  name: Openapi List Tags For Resource Response Example
  slug: openapi-list-tags-for-resource-response-example
- key_count: 0
  name: Openapi Manifest Overrides Payload Data Example
  slug: openapi-manifest-overrides-payload-data-example
- key_count: 1
  name: Openapi Manifest Overrides Payload Example
  slug: openapi-manifest-overrides-payload-example
- key_count: 0
  name: Openapi Manifest Payload Data Example
  slug: openapi-manifest-payload-data-example
- key_count: 1
  name: Openapi Manifest Payload Example
  slug: openapi-manifest-payload-example
- key_count: 0
  name: Openapi Mark Latest Patch Example
  slug: openapi-mark-latest-patch-example
- key_count: 0
  name: Openapi Mask Example
  slug: openapi-mask-example
- key_count: 0
  name: Openapi Max Connections Example
  slug: openapi-max-connections-example
- key_count: 0
  name: Openapi Max Size25 Example
  slug: openapi-max-size25-example
- key_count: 0
  name: Openapi Name Filter Example
  slug: openapi-name-filter-example
- key_count: 0
  name: Openapi Network Connection Status Example
  slug: openapi-network-connection-status-example
- key_count: 3
  name: Openapi Network Payload Example
  slug: openapi-network-payload-example
- key_count: 4
  name: Openapi Network Status Example
  slug: openapi-network-status-example
- key_count: 0
  name: Openapi Next Token Example
  slug: openapi-next-token-example
- key_count: 0
  name: Openapi Node Asset Name Example
  slug: openapi-node-asset-name-example
- key_count: 0
  name: Openapi Node Category Example
  slug: openapi-node-category-example
- key_count: 11
  name: Openapi Node Example
  slug: openapi-node-example
- key_count: 6
  name: Openapi Node From Template Job Example
  slug: openapi-node-from-template-job-example
- key_count: 0
  name: Openapi Node From Template Job Status Example
  slug: openapi-node-from-template-job-status-example
- key_count: 0
  name: Openapi Node From Template Job Status Message Example
  slug: openapi-node-from-template-job-status-message-example
- key_count: 0
  name: Openapi Node Id Example
  slug: openapi-node-id-example
- key_count: 5
  name: Openapi Node Input Port Example
  slug: openapi-node-input-port-example
- key_count: 7
  name: Openapi Node Instance Example
  slug: openapi-node-instance-example
- key_count: 0
  name: Openapi Node Instance Id Example
  slug: openapi-node-instance-id-example
- key_count: 0
  name: Openapi Node Instance Status Example
  slug: openapi-node-instance-status-example
- key_count: 2
  name: Openapi Node Interface Example
  slug: openapi-node-interface-example
- key_count: 0
  name: Openapi Node Name Example
  slug: openapi-node-name-example
- key_count: 3
  name: Openapi Node Output Port Example
  slug: openapi-node-output-port-example
- key_count: 0
  name: Openapi Node Package Arn Example
  slug: openapi-node-package-arn-example
- key_count: 0
  name: Openapi Node Package Id Example
  slug: openapi-node-package-id-example
- key_count: 0
  name: Openapi Node Package Name Example
  slug: openapi-node-package-name-example
- key_count: 0
  name: Openapi Node Package Patch Version Example
  slug: openapi-node-package-patch-version-example
- key_count: 0
  name: Openapi Node Package Version Example
  slug: openapi-node-package-version-example
- key_count: 2
  name: Openapi Node Signal Example
  slug: openapi-node-signal-example
- key_count: 0
  name: Openapi Node Signal Value Example
  slug: openapi-node-signal-value-example
- key_count: 1
  name: Openapi Ntp Payload Example
  slug: openapi-ntp-payload-example
- key_count: 0
  name: Openapi Ntp Server Name Example
  slug: openapi-ntp-server-name-example
- key_count: 3
  name: Openapi Ntp Status Example
  slug: openapi-ntp-status-example
- key_count: 0
  name: Openapi Object Example
  slug: openapi-object-example
- key_count: 0
  name: Openapi Object Key Example
  slug: openapi-object-key-example
- key_count: 2
  name: Openapi Ota Job Config Example
  slug: openapi-ota-job-config-example
- key_count: 2
  name: Openapi Out Put S3 Location Example
  slug: openapi-out-put-s3-location-example
- key_count: 6
  name: Openapi Package Import Job Example
  slug: openapi-package-import-job-example
- key_count: 1
  name: Openapi Package Import Job Input Config Example
  slug: openapi-package-import-job-input-config-example
- key_count: 1
  name: Openapi Package Import Job Output Config Example
  slug: openapi-package-import-job-output-config-example
- key_count: 4
  name: Openapi Package Import Job Output Example
  slug: openapi-package-import-job-output-example
- key_count: 0
  name: Openapi Package Import Job Status Example
  slug: openapi-package-import-job-status-example
- key_count: 0
  name: Openapi Package Import Job Status Message Example
  slug: openapi-package-import-job-status-message-example
- key_count: 0
  name: Openapi Package Import Job Type Example
  slug: openapi-package-import-job-type-example
- key_count: 5
  name: Openapi Package List Item Example
  slug: openapi-package-list-item-example
- key_count: 3
  name: Openapi Package Object Example
  slug: openapi-package-object-example
- key_count: 0
  name: Openapi Package Owner Account Example
  slug: openapi-package-owner-account-example
- key_count: 1
  name: Openapi Package Version Input Config Example
  slug: openapi-package-version-input-config-example
- key_count: 3
  name: Openapi Package Version Output Config Example
  slug: openapi-package-version-output-config-example
- key_count: 0
  name: Openapi Package Version Status Description Example
  slug: openapi-package-version-status-description-example
- key_count: 0
  name: Openapi Package Version Status Example
  slug: openapi-package-version-status-example
- key_count: 0
  name: Openapi Port Default Value Example
  slug: openapi-port-default-value-example
- key_count: 0
  name: Openapi Port Name Example
  slug: openapi-port-name-example
- key_count: 0
  name: Openapi Port Type Example
  slug: openapi-port-type-example
- key_count: 0
  name: Openapi Principal Arn Example
  slug: openapi-principal-arn-example
- key_count: 4
  name: Openapi Provision Device Request Example
  slug: openapi-provision-device-request-example
- key_count: 5
  name: Openapi Provision Device Response Example
  slug: openapi-provision-device-response-example
- key_count: 0
  name: Openapi Region Example
  slug: openapi-region-example
- key_count: 2
  name: Openapi Register Package Version Request Example
  slug: openapi-register-package-version-request-example
- key_count: 0
  name: Openapi Register Package Version Response Example
  slug: openapi-register-package-version-response-example
- key_count: 0
  name: Openapi Remove Application Instance Request Example
  slug: openapi-remove-application-instance-request-example
- key_count: 0
  name: Openapi Remove Application Instance Response Example
  slug: openapi-remove-application-instance-response-example
- key_count: 4
  name: Openapi Reported Runtime Context State Example
  slug: openapi-reported-runtime-context-state-example
- key_count: 0
  name: Openapi Resource Arn Example
  slug: openapi-resource-arn-example
- key_count: 0
  name: Openapi Resource Not Found Exception Example
  slug: openapi-resource-not-found-exception-example
- key_count: 0
  name: Openapi Runtime Context Name Example
  slug: openapi-runtime-context-name-example
- key_count: 0
  name: Openapi Runtime Role Arn Example
  slug: openapi-runtime-role-arn-example
- key_count: 3
  name: Openapi S3 Location Example
  slug: openapi-s3-location-example
- key_count: 0
  name: Openapi Service Quota Exceeded Exception Example
  slug: openapi-service-quota-exceeded-exception-example
- key_count: 1
  name: Openapi Signal Application Instance Node Instances Request Example
  slug: openapi-signal-application-instance-node-instances-request-example
- key_count: 1
  name: Openapi Signal Application Instance Node Instances Response Example
  slug: openapi-signal-application-instance-node-instances-response-example
- key_count: 0
  name: Openapi Sort Order Example
  slug: openapi-sort-order-example
- key_count: 4
  name: Openapi Static Ip Connection Info Example
  slug: openapi-static-ip-connection-info-example
- key_count: 0
  name: Openapi Status Filter Example
  slug: openapi-status-filter-example
- key_count: 5
  name: Openapi Storage Location Example
  slug: openapi-storage-location-example
- key_count: 0
  name: Openapi Tag Key Example
  slug: openapi-tag-key-example
- key_count: 0
  name: Openapi Tag Map Example
  slug: openapi-tag-map-example
- key_count: 1
  name: Openapi Tag Resource Request Example
  slug: openapi-tag-resource-request-example
- key_count: 0
  name: Openapi Tag Resource Response Example
  slug: openapi-tag-resource-response-example
- key_count: 0
  name: Openapi Tag Value Example
  slug: openapi-tag-value-example
- key_count: 0
  name: Openapi Template Key Example
  slug: openapi-template-key-example
- key_count: 0
  name: Openapi Template Parameters Map Example
  slug: openapi-template-parameters-map-example
- key_count: 0
  name: Openapi Template Type Example
  slug: openapi-template-type-example
- key_count: 0
  name: Openapi Template Value Example
  slug: openapi-template-value-example
- key_count: 0
  name: Openapi Time Stamp Example
  slug: openapi-time-stamp-example
- key_count: 0
  name: Openapi Token Example
  slug: openapi-token-example
- key_count: 0
  name: Openapi Untag Resource Request Example
  slug: openapi-untag-resource-request-example
- key_count: 0
  name: Openapi Untag Resource Response Example
  slug: openapi-untag-resource-response-example
- key_count: 0
  name: Openapi Update Created Time Example
  slug: openapi-update-created-time-example
- key_count: 1
  name: Openapi Update Device Metadata Request Example
  slug: openapi-update-device-metadata-request-example
- key_count: 1
  name: Openapi Update Device Metadata Response Example
  slug: openapi-update-device-metadata-response-example
- key_count: 0
  name: Openapi Update Progress Example
  slug: openapi-update-progress-example
- key_count: 0
  name: Openapi Validation Exception Example
  slug: openapi-validation-exception-example
- key_count: 0
  name: Openapi Version Example
  slug: openapi-version-example
finops:
- name: Amazon Panorama Finops
  service_category: API
  slug: amazon-panorama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-panorama.png
json_schemas:
- name: AccessDeniedException
  property_count: 0
  slug: openapi-access-denied-exception
- name: AlternateSoftwareMetadata
  property_count: 1
  slug: openapi-alternate-software-metadata
- name: AlternateSoftwares
  property_count: 0
  slug: openapi-alternate-softwares
- name: ApplicationInstanceArn
  property_count: 0
  slug: openapi-application-instance-arn
- name: ApplicationInstanceHealthStatus
  property_count: 0
  slug: openapi-application-instance-health-status
- name: ApplicationInstanceId
  property_count: 0
  slug: openapi-application-instance-id
- name: ApplicationInstanceName
  property_count: 0
  slug: openapi-application-instance-name
- name: ApplicationInstance
  property_count: 12
  slug: openapi-application-instance
- name: ApplicationInstanceStatusDescription
  property_count: 0
  slug: openapi-application-instance-status-description
- name: ApplicationInstanceStatus
  property_count: 0
  slug: openapi-application-instance-status
- name: ApplicationInstances
  property_count: 0
  slug: openapi-application-instances
- name: Boolean
  property_count: 0
  slug: openapi-boolean
- name: BucketName
  property_count: 0
  slug: openapi-bucket-name
- name: Bucket
  property_count: 0
  slug: openapi-bucket
- name: Certificates
  property_count: 0
  slug: openapi-certificates
- name: ClientToken
  property_count: 0
  slug: openapi-client-token
- name: ConflictException
  property_count: 0
  slug: openapi-conflict-exception
- name: ConnectionType
  property_count: 0
  slug: openapi-connection-type
- name: CreateApplicationInstanceRequest
  property_count: 8
  slug: openapi-create-application-instance-request
- name: CreateApplicationInstanceResponse
  property_count: 1
  slug: openapi-create-application-instance-response
- name: CreateJobForDevicesRequest
  property_count: 3
  slug: openapi-create-job-for-devices-request
- name: CreateJobForDevicesResponse
  property_count: 1
  slug: openapi-create-job-for-devices-response
- name: CreateNodeFromTemplateJobRequest
  property_count: 7
  slug: openapi-create-node-from-template-job-request
- name: CreateNodeFromTemplateJobResponse
  property_count: 1
  slug: openapi-create-node-from-template-job-response
- name: CreatePackageImportJobRequest
  property_count: 5
  slug: openapi-create-package-import-job-request
- name: CreatePackageImportJobResponse
  property_count: 1
  slug: openapi-create-package-import-job-response
- name: CreatePackageRequest
  property_count: 2
  slug: openapi-create-package-request
- name: CreatePackageResponse
  property_count: 3
  slug: openapi-create-package-response
- name: CreatedTime
  property_count: 0
  slug: openapi-created-time
- name: CurrentSoftware
  property_count: 0
  slug: openapi-current-software
- name: DefaultGateway
  property_count: 0
  slug: openapi-default-gateway
- name: DefaultRuntimeContextDevice
  property_count: 0
  slug: openapi-default-runtime-context-device
- name: DeleteDeviceRequest
  property_count: 0
  slug: openapi-delete-device-request
- name: DeleteDeviceResponse
  property_count: 1
  slug: openapi-delete-device-response
- name: DeletePackageRequest
  property_count: 0
  slug: openapi-delete-package-request
- name: DeletePackageResponse
  property_count: 0
  slug: openapi-delete-package-response
- name: DeregisterPackageVersionRequest
  property_count: 0
  slug: openapi-deregister-package-version-request
- name: DeregisterPackageVersionResponse
  property_count: 0
  slug: openapi-deregister-package-version-response
- name: DescribeApplicationInstanceDetailsRequest
  property_count: 0
  slug: openapi-describe-application-instance-details-request
- name: DescribeApplicationInstanceDetailsResponse
  property_count: 8
  slug: openapi-describe-application-instance-details-response
- name: DescribeApplicationInstanceRequest
  property_count: 0
  slug: openapi-describe-application-instance-request
- name: DescribeApplicationInstanceResponse
  property_count: 15
  slug: openapi-describe-application-instance-response
- name: DescribeDeviceJobRequest
  property_count: 0
  slug: openapi-describe-device-job-request
- name: DescribeDeviceJobResponse
  property_count: 9
  slug: openapi-describe-device-job-response
- name: DescribeDeviceRequest
  property_count: 0
  slug: openapi-describe-device-request
- name: DescribeDeviceResponse
  property_count: 20
  slug: openapi-describe-device-response
- name: DescribeNodeFromTemplateJobRequest
  property_count: 0
  slug: openapi-describe-node-from-template-job-request
- name: DescribeNodeFromTemplateJobResponse
  property_count: 12
  slug: openapi-describe-node-from-template-job-response
- name: DescribeNodeRequest
  property_count: 0
  slug: openapi-describe-node-request
- name: DescribeNodeResponse
  property_count: 14
  slug: openapi-describe-node-response
- name: DescribePackageImportJobRequest
  property_count: 0
  slug: openapi-describe-package-import-job-request
- name: DescribePackageImportJobResponse
  property_count: 11
  slug: openapi-describe-package-import-job-response
- name: DescribePackageRequest
  property_count: 0
  slug: openapi-describe-package-request
- name: DescribePackageResponse
  property_count: 8
  slug: openapi-describe-package-response
- name: DescribePackageVersionRequest
  property_count: 0
  slug: openapi-describe-package-version-request
- name: DescribePackageVersionResponse
  property_count: 10
  slug: openapi-describe-package-version-response
- name: Description
  property_count: 0
  slug: openapi-description
- name: DesiredState
  property_count: 0
  slug: openapi-desired-state
- name: DeviceAggregatedStatus
  property_count: 0
  slug: openapi-device-aggregated-status
- name: DeviceArn
  property_count: 0
  slug: openapi-device-arn
- name: DeviceBrand
  property_count: 0
  slug: openapi-device-brand
- name: DeviceConnectionStatus
  property_count: 0
  slug: openapi-device-connection-status
- name: DeviceIdList
  property_count: 0
  slug: openapi-device-id-list
- name: DeviceId
  property_count: 0
  slug: openapi-device-id
- name: DeviceJobConfig
  property_count: 1
  slug: openapi-device-job-config
- name: DeviceJobList
  property_count: 0
  slug: openapi-device-job-list
- name: DeviceJob
  property_count: 5
  slug: openapi-device-job
- name: DeviceList
  property_count: 0
  slug: openapi-device-list
- name: DeviceName
  property_count: 0
  slug: openapi-device-name
- name: DeviceReportedStatus
  property_count: 0
  slug: openapi-device-reported-status
- name: Device
  property_count: 13
  slug: openapi-device
- name: DeviceSerialNumber
  property_count: 0
  slug: openapi-device-serial-number
- name: DeviceStatus
  property_count: 0
  slug: openapi-device-status
- name: DeviceType
  property_count: 0
  slug: openapi-device-type
- name: DnsList
  property_count: 0
  slug: openapi-dns-list
- name: Dns
  property_count: 0
  slug: openapi-dns
- name: EthernetPayload
  property_count: 2
  slug: openapi-ethernet-payload
- name: EthernetStatus
  property_count: 3
  slug: openapi-ethernet-status
- name: HwAddress
  property_count: 0
  slug: openapi-hw-address
- name: ImageVersion
  property_count: 0
  slug: openapi-image-version
- name: InputPortList
  property_count: 0
  slug: openapi-input-port-list
- name: InternalServerException
  property_count: 0
  slug: openapi-internal-server-exception
- name: IotThingName
  property_count: 0
  slug: openapi-iot-thing-name
- name: IpAddressOrServerName
  property_count: 0
  slug: openapi-ip-address-or-server-name
- name: IpAddress
  property_count: 0
  slug: openapi-ip-address
- name: JobId
  property_count: 0
  slug: openapi-job-id
- name: JobList
  property_count: 0
  slug: openapi-job-list
- name: JobResourceTags
  property_count: 2
  slug: openapi-job-resource-tags
- name: JobResourceType
  property_count: 0
  slug: openapi-job-resource-type
- name: Job
  property_count: 2
  slug: openapi-job
- name: JobTagsList
  property_count: 0
  slug: openapi-job-tags-list
- name: JobType
  property_count: 0
  slug: openapi-job-type
- name: LastUpdatedTime
  property_count: 0
  slug: openapi-last-updated-time
- name: LatestAlternateSoftware
  property_count: 0
  slug: openapi-latest-alternate-software
- name: LatestDeviceJob
  property_count: 3
  slug: openapi-latest-device-job
- name: LatestSoftware
  property_count: 0
  slug: openapi-latest-software
- name: LeaseExpirationTime
  property_count: 0
  slug: openapi-lease-expiration-time
- name: ListApplicationInstanceDependenciesRequest
  property_count: 0
  slug: openapi-list-application-instance-dependencies-request
- name: ListApplicationInstanceDependenciesResponse
  property_count: 2
  slug: openapi-list-application-instance-dependencies-response
- name: ListApplicationInstanceNodeInstancesRequest
  property_count: 0
  slug: openapi-list-application-instance-node-instances-request
- name: ListApplicationInstanceNodeInstancesResponse
  property_count: 2
  slug: openapi-list-application-instance-node-instances-response
- name: ListApplicationInstancesRequest
  property_count: 0
  slug: openapi-list-application-instances-request
- name: ListApplicationInstancesResponse
  property_count: 2
  slug: openapi-list-application-instances-response
- name: ListDevicesJobsRequest
  property_count: 0
  slug: openapi-list-devices-jobs-request
- name: ListDevicesJobsResponse
  property_count: 2
  slug: openapi-list-devices-jobs-response
- name: ListDevicesRequest
  property_count: 0
  slug: openapi-list-devices-request
- name: ListDevicesResponse
  property_count: 2
  slug: openapi-list-devices-response
- name: ListDevicesSortBy
  property_count: 0
  slug: openapi-list-devices-sort-by
- name: ListNodeFromTemplateJobsRequest
  property_count: 0
  slug: openapi-list-node-from-template-jobs-request
- name: ListNodeFromTemplateJobsResponse
  property_count: 2
  slug: openapi-list-node-from-template-jobs-response
- name: ListNodesRequest
  property_count: 0
  slug: openapi-list-nodes-request
- name: ListNodesResponse
  property_count: 2
  slug: openapi-list-nodes-response
- name: ListPackageImportJobsRequest
  property_count: 0
  slug: openapi-list-package-import-jobs-request
- name: ListPackageImportJobsResponse
  property_count: 2
  slug: openapi-list-package-import-jobs-response
- name: ListPackagesRequest
  property_count: 0
  slug: openapi-list-packages-request
- name: ListPackagesResponse
  property_count: 2
  slug: openapi-list-packages-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: openapi-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: openapi-list-tags-for-resource-response
- name: ManifestOverridesPayloadData
  property_count: 0
  slug: openapi-manifest-overrides-payload-data
- name: ManifestOverridesPayload
  property_count: 1
  slug: openapi-manifest-overrides-payload
- name: ManifestPayloadData
  property_count: 0
  slug: openapi-manifest-payload-data
- name: ManifestPayload
  property_count: 1
  slug: openapi-manifest-payload
- name: MarkLatestPatch
  property_count: 0
  slug: openapi-mark-latest-patch
- name: Mask
  property_count: 0
  slug: openapi-mask
- name: MaxConnections
  property_count: 0
  slug: openapi-max-connections
- name: MaxSize25
  property_count: 0
  slug: openapi-max-size25
- name: NameFilter
  property_count: 0
  slug: openapi-name-filter
- name: NetworkConnectionStatus
  property_count: 0
  slug: openapi-network-connection-status
- name: NetworkPayload
  property_count: 3
  slug: openapi-network-payload
- name: NetworkStatus
  property_count: 4
  slug: openapi-network-status
- name: NextToken
  property_count: 0
  slug: openapi-next-token
- name: NodeAssetName
  property_count: 0
  slug: openapi-node-asset-name
- name: NodeCategory
  property_count: 0
  slug: openapi-node-category
- name: NodeFromTemplateJobList
  property_count: 0
  slug: openapi-node-from-template-job-list
- name: NodeFromTemplateJob
  property_count: 6
  slug: openapi-node-from-template-job
- name: NodeFromTemplateJobStatusMessage
  property_count: 0
  slug: openapi-node-from-template-job-status-message
- name: NodeFromTemplateJobStatus
  property_count: 0
  slug: openapi-node-from-template-job-status
- name: NodeId
  property_count: 0
  slug: openapi-node-id
- name: NodeInputPort
  property_count: 5
  slug: openapi-node-input-port
- name: NodeInstanceId
  property_count: 0
  slug: openapi-node-instance-id
- name: NodeInstance
  property_count: 7
  slug: openapi-node-instance
- name: NodeInstanceStatus
  property_count: 0
  slug: openapi-node-instance-status
- name: NodeInstances
  property_count: 0
  slug: openapi-node-instances
- name: NodeInterface
  property_count: 2
  slug: openapi-node-interface
- name: NodeName
  property_count: 0
  slug: openapi-node-name
- name: NodeOutputPort
  property_count: 3
  slug: openapi-node-output-port
- name: NodePackageArn
  property_count: 0
  slug: openapi-node-package-arn
- name: NodePackageId
  property_count: 0
  slug: openapi-node-package-id
- name: NodePackageName
  property_count: 0
  slug: openapi-node-package-name
- name: NodePackagePatchVersion
  property_count: 0
  slug: openapi-node-package-patch-version
- name: NodePackageVersion
  property_count: 0
  slug: openapi-node-package-version
- name: Node
  property_count: 11
  slug: openapi-node
- name: NodeSignalList
  property_count: 0
  slug: openapi-node-signal-list
- name: NodeSignal
  property_count: 2
  slug: openapi-node-signal
- name: NodeSignalValue
  property_count: 0
  slug: openapi-node-signal-value
- name: NodesList
  property_count: 0
  slug: openapi-nodes-list
- name: NtpPayload
  property_count: 1
  slug: openapi-ntp-payload
- name: NtpServerList
  property_count: 0
  slug: openapi-ntp-server-list
- name: NtpServerName
  property_count: 0
  slug: openapi-ntp-server-name
- name: NtpStatus
  property_count: 3
  slug: openapi-ntp-status
- name: ObjectKey
  property_count: 0
  slug: openapi-object-key
- name: Object
  property_count: 0
  slug: openapi-object
- name: OTAJobConfig
  property_count: 2
  slug: openapi-ota-job-config
- name: OutPutS3Location
  property_count: 2
  slug: openapi-out-put-s3-location
- name: OutputPortList
  property_count: 0
  slug: openapi-output-port-list
- name: PackageImportJobInputConfig
  property_count: 1
  slug: openapi-package-import-job-input-config
- name: PackageImportJobList
  property_count: 0
  slug: openapi-package-import-job-list
- name: PackageImportJobOutputConfig
  property_count: 1
  slug: openapi-package-import-job-output-config
- name: PackageImportJobOutput
  property_count: 4
  slug: openapi-package-import-job-output
- name: PackageImportJob
  property_count: 6
  slug: openapi-package-import-job
- name: PackageImportJobStatusMessage
  property_count: 0
  slug: openapi-package-import-job-status-message
- name: PackageImportJobStatus
  property_count: 0
  slug: openapi-package-import-job-status
- name: PackageImportJobType
  property_count: 0
  slug: openapi-package-import-job-type
- name: PackageListItem
  property_count: 5
  slug: openapi-package-list-item
- name: PackageList
  property_count: 0
  slug: openapi-package-list
- name: PackageObject
  property_count: 3
  slug: openapi-package-object
- name: PackageObjects
  property_count: 0
  slug: openapi-package-objects
- name: PackageOwnerAccount
  property_count: 0
  slug: openapi-package-owner-account
- name: PackageVersionInputConfig
  property_count: 1
  slug: openapi-package-version-input-config
- name: PackageVersionOutputConfig
  property_count: 3
  slug: openapi-package-version-output-config
- name: PackageVersionStatusDescription
  property_count: 0
  slug: openapi-package-version-status-description
- name: PackageVersionStatus
  property_count: 0
  slug: openapi-package-version-status
- name: PortDefaultValue
  property_count: 0
  slug: openapi-port-default-value
- name: PortName
  property_count: 0
  slug: openapi-port-name
- name: PortType
  property_count: 0
  slug: openapi-port-type
- name: PrincipalArn
  property_count: 0
  slug: openapi-principal-arn
- name: PrincipalArnsList
  property_count: 0
  slug: openapi-principal-arns-list
- name: ProvisionDeviceRequest
  property_count: 4
  slug: openapi-provision-device-request
- name: ProvisionDeviceResponse
  property_count: 5
  slug: openapi-provision-device-response
- name: Region
  property_count: 0
  slug: openapi-region
- name: RegisterPackageVersionRequest
  property_count: 2
  slug: openapi-register-package-version-request
- name: RegisterPackageVersionResponse
  property_count: 0
  slug: openapi-register-package-version-response
- name: RemoveApplicationInstanceRequest
  property_count: 0
  slug: openapi-remove-application-instance-request
- name: RemoveApplicationInstanceResponse
  property_count: 0
  slug: openapi-remove-application-instance-response
- name: ReportedRuntimeContextState
  property_count: 4
  slug: openapi-reported-runtime-context-state
- name: ReportedRuntimeContextStates
  property_count: 0
  slug: openapi-reported-runtime-context-states
- name: ResourceArn
  property_count: 0
  slug: openapi-resource-arn
- name: ResourceNotFoundException
  property_count: 0
  slug: openapi-resource-not-found-exception
- name: RuntimeContextName
  property_count: 0
  slug: openapi-runtime-context-name
- name: RuntimeRoleArn
  property_count: 0
  slug: openapi-runtime-role-arn
- name: S3Location
  property_count: 3
  slug: openapi-s3-location
- name: ServiceQuotaExceededException
  property_count: 0
  slug: openapi-service-quota-exceeded-exception
- name: SignalApplicationInstanceNodeInstancesRequest
  property_count: 1
  slug: openapi-signal-application-instance-node-instances-request
- name: SignalApplicationInstanceNodeInstancesResponse
  property_count: 1
  slug: openapi-signal-application-instance-node-instances-response
- name: SortOrder
  property_count: 0
  slug: openapi-sort-order
- name: StaticIpConnectionInfo
  property_count: 4
  slug: openapi-static-ip-connection-info
- name: StatusFilter
  property_count: 0
  slug: openapi-status-filter
- name: StorageLocation
  property_count: 5
  slug: openapi-storage-location
- name: TagKeyList
  property_count: 0
  slug: openapi-tag-key-list
- name: TagKey
  property_count: 0
  slug: openapi-tag-key
- name: TagMap
  property_count: 0
  slug: openapi-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: openapi-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: openapi-tag-resource-response
- name: TagValue
  property_count: 0
  slug: openapi-tag-value
- name: TemplateKey
  property_count: 0
  slug: openapi-template-key
- name: TemplateParametersMap
  property_count: 0
  slug: openapi-template-parameters-map
- name: TemplateType
  property_count: 0
  slug: openapi-template-type
- name: TemplateValue
  property_count: 0
  slug: openapi-template-value
- name: TimeStamp
  property_count: 0
  slug: openapi-time-stamp
- name: Token
  property_count: 0
  slug: openapi-token
- name: UntagResourceRequest
  property_count: 0
  slug: openapi-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: openapi-untag-resource-response
- name: UpdateCreatedTime
  property_count: 0
  slug: openapi-update-created-time
- name: UpdateDeviceMetadataRequest
  property_count: 1
  slug: openapi-update-device-metadata-request
- name: UpdateDeviceMetadataResponse
  property_count: 1
  slug: openapi-update-device-metadata-response
- name: UpdateProgress
  property_count: 0
  slug: openapi-update-progress
- name: ValidationException
  property_count: 0
  slug: openapi-validation-exception
- name: Version
  property_count: 0
  slug: openapi-version
json_structures:
- name: Openapi Access Denied Exception Structure
  property_count: 0
  slug: openapi-access-denied-exception-structure
- name: Openapi Alternate Software Metadata Structure
  property_count: 1
  slug: openapi-alternate-software-metadata-structure
- name: Openapi Alternate Softwares Structure
  property_count: 0
  slug: openapi-alternate-softwares-structure
- name: Openapi Application Instance Arn Structure
  property_count: 0
  slug: openapi-application-instance-arn-structure
- name: Openapi Application Instance Health Status Structure
  property_count: 0
  slug: openapi-application-instance-health-status-structure
- name: Openapi Application Instance Id Structure
  property_count: 0
  slug: openapi-application-instance-id-structure
- name: Openapi Application Instance Name Structure
  property_count: 0
  slug: openapi-application-instance-name-structure
- name: Openapi Application Instance Status Description Structure
  property_count: 0
  slug: openapi-application-instance-status-description-structure
- name: Openapi Application Instance Status Structure
  property_count: 0
  slug: openapi-application-instance-status-structure
- name: Openapi Application Instance Structure
  property_count: 12
  slug: openapi-application-instance-structure
- name: Openapi Application Instances Structure
  property_count: 0
  slug: openapi-application-instances-structure
- name: Openapi Boolean Structure
  property_count: 0
  slug: openapi-boolean-structure
- name: Openapi Bucket Name Structure
  property_count: 0
  slug: openapi-bucket-name-structure
- name: Openapi Bucket Structure
  property_count: 0
  slug: openapi-bucket-structure
- name: Openapi Certificates Structure
  property_count: 0
  slug: openapi-certificates-structure
- name: Openapi Client Token Structure
  property_count: 0
  slug: openapi-client-token-structure
- name: Openapi Conflict Exception Structure
  property_count: 0
  slug: openapi-conflict-exception-structure
- name: Openapi Connection Type Structure
  property_count: 0
  slug: openapi-connection-type-structure
- name: Openapi Create Application Instance Request Structure
  property_count: 8
  slug: openapi-create-application-instance-request-structure
- name: Openapi Create Application Instance Response Structure
  property_count: 1
  slug: openapi-create-application-instance-response-structure
- name: Openapi Create Job For Devices Request Structure
  property_count: 3
  slug: openapi-create-job-for-devices-request-structure
- name: Openapi Create Job For Devices Response Structure
  property_count: 1
  slug: openapi-create-job-for-devices-response-structure
- name: Openapi Create Node From Template Job Request Structure
  property_count: 7
  slug: openapi-create-node-from-template-job-request-structure
- name: Openapi Create Node From Template Job Response Structure
  property_count: 1
  slug: openapi-create-node-from-template-job-response-structure
- name: Openapi Create Package Import Job Request Structure
  property_count: 5
  slug: openapi-create-package-import-job-request-structure
- name: Openapi Create Package Import Job Response Structure
  property_count: 1
  slug: openapi-create-package-import-job-response-structure
- name: Openapi Create Package Request Structure
  property_count: 2
  slug: openapi-create-package-request-structure
- name: Openapi Create Package Response Structure
  property_count: 3
  slug: openapi-create-package-response-structure
- name: Openapi Created Time Structure
  property_count: 0
  slug: openapi-created-time-structure
- name: Openapi Current Software Structure
  property_count: 0
  slug: openapi-current-software-structure
- name: Openapi Default Gateway Structure
  property_count: 0
  slug: openapi-default-gateway-structure
- name: Openapi Default Runtime Context Device Structure
  property_count: 0
  slug: openapi-default-runtime-context-device-structure
- name: Openapi Delete Device Request Structure
  property_count: 0
  slug: openapi-delete-device-request-structure
- name: Openapi Delete Device Response Structure
  property_count: 1
  slug: openapi-delete-device-response-structure
- name: Openapi Delete Package Request Structure
  property_count: 0
  slug: openapi-delete-package-request-structure
- name: Openapi Delete Package Response Structure
  property_count: 0
  slug: openapi-delete-package-response-structure
- name: Openapi Deregister Package Version Request Structure
  property_count: 0
  slug: openapi-deregister-package-version-request-structure
- name: Openapi Deregister Package Version Response Structure
  property_count: 0
  slug: openapi-deregister-package-version-response-structure
- name: Openapi Describe Application Instance Details Request Structure
  property_count: 0
  slug: openapi-describe-application-instance-details-request-structure
- name: Openapi Describe Application Instance Details Response Structure
  property_count: 8
  slug: openapi-describe-application-instance-details-response-structure
- name: Openapi Describe Application Instance Request Structure
  property_count: 0
  slug: openapi-describe-application-instance-request-structure
- name: Openapi Describe Application Instance Response Structure
  property_count: 15
  slug: openapi-describe-application-instance-response-structure
- name: Openapi Describe Device Job Request Structure
  property_count: 0
  slug: openapi-describe-device-job-request-structure
- name: Openapi Describe Device Job Response Structure
  property_count: 9
  slug: openapi-describe-device-job-response-structure
- name: Openapi Describe Device Request Structure
  property_count: 0
  slug: openapi-describe-device-request-structure
- name: Openapi Describe Device Response Structure
  property_count: 20
  slug: openapi-describe-device-response-structure
- name: Openapi Describe Node From Template Job Request Structure
  property_count: 0
  slug: openapi-describe-node-from-template-job-request-structure
- name: Openapi Describe Node From Template Job Response Structure
  property_count: 12
  slug: openapi-describe-node-from-template-job-response-structure
- name: Openapi Describe Node Request Structure
  property_count: 0
  slug: openapi-describe-node-request-structure
- name: Openapi Describe Node Response Structure
  property_count: 14
  slug: openapi-describe-node-response-structure
- name: Openapi Describe Package Import Job Request Structure
  property_count: 0
  slug: openapi-describe-package-import-job-request-structure
- name: Openapi Describe Package Import Job Response Structure
  property_count: 11
  slug: openapi-describe-package-import-job-response-structure
- name: Openapi Describe Package Request Structure
  property_count: 0
  slug: openapi-describe-package-request-structure
- name: Openapi Describe Package Response Structure
  property_count: 8
  slug: openapi-describe-package-response-structure
- name: Openapi Describe Package Version Request Structure
  property_count: 0
  slug: openapi-describe-package-version-request-structure
- name: Openapi Describe Package Version Response Structure
  property_count: 10
  slug: openapi-describe-package-version-response-structure
- name: Openapi Description Structure
  property_count: 0
  slug: openapi-description-structure
- name: Openapi Desired State Structure
  property_count: 0
  slug: openapi-desired-state-structure
- name: Openapi Device Aggregated Status Structure
  property_count: 0
  slug: openapi-device-aggregated-status-structure
- name: Openapi Device Arn Structure
  property_count: 0
  slug: openapi-device-arn-structure
- name: Openapi Device Brand Structure
  property_count: 0
  slug: openapi-device-brand-structure
- name: Openapi Device Connection Status Structure
  property_count: 0
  slug: openapi-device-connection-status-structure
- name: Openapi Device Id List Structure
  property_count: 0
  slug: openapi-device-id-list-structure
- name: Openapi Device Id Structure
  property_count: 0
  slug: openapi-device-id-structure
- name: Openapi Device Job Config Structure
  property_count: 1
  slug: openapi-device-job-config-structure
- name: Openapi Device Job List Structure
  property_count: 0
  slug: openapi-device-job-list-structure
- name: Openapi Device Job Structure
  property_count: 5
  slug: openapi-device-job-structure
- name: Openapi Device List Structure
  property_count: 0
  slug: openapi-device-list-structure
- name: Openapi Device Name Structure
  property_count: 0
  slug: openapi-device-name-structure
- name: Openapi Device Reported Status Structure
  property_count: 0
  slug: openapi-device-reported-status-structure
- name: Openapi Device Serial Number Structure
  property_count: 0
  slug: openapi-device-serial-number-structure
- name: Openapi Device Status Structure
  property_count: 0
  slug: openapi-device-status-structure
- name: Openapi Device Structure
  property_count: 13
  slug: openapi-device-structure
- name: Openapi Device Type Structure
  property_count: 0
  slug: openapi-device-type-structure
- name: Openapi Dns List Structure
  property_count: 0
  slug: openapi-dns-list-structure
- name: Openapi Dns Structure
  property_count: 0
  slug: openapi-dns-structure
- name: Openapi Ethernet Payload Structure
  property_count: 2
  slug: openapi-ethernet-payload-structure
- name: Openapi Ethernet Status Structure
  property_count: 3
  slug: openapi-ethernet-status-structure
- name: Openapi Hw Address Structure
  property_count: 0
  slug: openapi-hw-address-structure
- name: Openapi Image Version Structure
  property_count: 0
  slug: openapi-image-version-structure
- name: Openapi Input Port List Structure
  property_count: 0
  slug: openapi-input-port-list-structure
- name: Openapi Internal Server Exception Structure
  property_count: 0
  slug: openapi-internal-server-exception-structure
- name: Openapi Iot Thing Name Structure
  property_count: 0
  slug: openapi-iot-thing-name-structure
- name: Openapi Ip Address Or Server Name Structure
  property_count: 0
  slug: openapi-ip-address-or-server-name-structure
- name: Openapi Ip Address Structure
  property_count: 0
  slug: openapi-ip-address-structure
- name: Openapi Job Id Structure
  property_count: 0
  slug: openapi-job-id-structure
- name: Openapi Job List Structure
  property_count: 0
  slug: openapi-job-list-structure
- name: Openapi Job Resource Tags Structure
  property_count: 2
  slug: openapi-job-resource-tags-structure
- name: Openapi Job Resource Type Structure
  property_count: 0
  slug: openapi-job-resource-type-structure
- name: Openapi Job Structure
  property_count: 2
  slug: openapi-job-structure
- name: Openapi Job Tags List Structure
  property_count: 0
  slug: openapi-job-tags-list-structure
- name: Openapi Job Type Structure
  property_count: 0
  slug: openapi-job-type-structure
- name: Openapi Last Updated Time Structure
  property_count: 0
  slug: openapi-last-updated-time-structure
- name: Openapi Latest Alternate Software Structure
  property_count: 0
  slug: openapi-latest-alternate-software-structure
- name: Openapi Latest Device Job Structure
  property_count: 3
  slug: openapi-latest-device-job-structure
- name: Openapi Latest Software Structure
  property_count: 0
  slug: openapi-latest-software-structure
- name: Openapi Lease Expiration Time Structure
  property_count: 0
  slug: openapi-lease-expiration-time-structure
- name: Openapi List Application Instance Dependencies Request Structure
  property_count: 0
  slug: openapi-list-application-instance-dependencies-request-structure
- name: Openapi List Application Instance Dependencies Response Structure
  property_count: 2
  slug: openapi-list-application-instance-dependencies-response-structure
- name: Openapi List Application Instance Node Instances Request Structure
  property_count: 0
  slug: openapi-list-application-instance-node-instances-request-structure
- name: Openapi List Application Instance Node Instances Response Structure
  property_count: 2
  slug: openapi-list-application-instance-node-instances-response-structure
- name: Openapi List Application Instances Request Structure
  property_count: 0
  slug: openapi-list-application-instances-request-structure
- name: Openapi List Application Instances Response Structure
  property_count: 2
  slug: openapi-list-application-instances-response-structure
- name: Openapi List Devices Jobs Request Structure
  property_count: 0
  slug: openapi-list-devices-jobs-request-structure
- name: Openapi List Devices Jobs Response Structure
  property_count: 2
  slug: openapi-list-devices-jobs-response-structure
- name: Openapi List Devices Request Structure
  property_count: 0
  slug: openapi-list-devices-request-structure
- name: Openapi List Devices Response Structure
  property_count: 2
  slug: openapi-list-devices-response-structure
- name: Openapi List Devices Sort By Structure
  property_count: 0
  slug: openapi-list-devices-sort-by-structure
- name: Openapi List Node From Template Jobs Request Structure
  property_count: 0
  slug: openapi-list-node-from-template-jobs-request-structure
- name: Openapi List Node From Template Jobs Response Structure
  property_count: 2
  slug: openapi-list-node-from-template-jobs-response-structure
- name: Openapi List Nodes Request Structure
  property_count: 0
  slug: openapi-list-nodes-request-structure
- name: Openapi List Nodes Response Structure
  property_count: 2
  slug: openapi-list-nodes-response-structure
- name: Openapi List Package Import Jobs Request Structure
  property_count: 0
  slug: openapi-list-package-import-jobs-request-structure
- name: Openapi List Package Import Jobs Response Structure
  property_count: 2
  slug: openapi-list-package-import-jobs-response-structure
- name: Openapi List Packages Request Structure
  property_count: 0
  slug: openapi-list-packages-request-structure
- name: Openapi List Packages Response Structure
  property_count: 2
  slug: openapi-list-packages-response-structure
- name: Openapi List Tags For Resource Request Structure
  property_count: 0
  slug: openapi-list-tags-for-resource-request-structure
- name: Openapi List Tags For Resource Response Structure
  property_count: 1
  slug: openapi-list-tags-for-resource-response-structure
- name: Openapi Manifest Overrides Payload Data Structure
  property_count: 0
  slug: openapi-manifest-overrides-payload-data-structure
- name: Openapi Manifest Overrides Payload Structure
  property_count: 1
  slug: openapi-manifest-overrides-payload-structure
- name: Openapi Manifest Payload Data Structure
  property_count: 0
  slug: openapi-manifest-payload-data-structure
- name: Openapi Manifest Payload Structure
  property_count: 1
  slug: openapi-manifest-payload-structure
- name: Openapi Mark Latest Patch Structure
  property_count: 0
  slug: openapi-mark-latest-patch-structure
- name: Openapi Mask Structure
  property_count: 0
  slug: openapi-mask-structure
- name: Openapi Max Connections Structure
  property_count: 0
  slug: openapi-max-connections-structure
- name: Openapi Max Size25 Structure
  property_count: 0
  slug: openapi-max-size25-structure
- name: Openapi Name Filter Structure
  property_count: 0
  slug: openapi-name-filter-structure
- name: Openapi Network Connection Status Structure
  property_count: 0
  slug: openapi-network-connection-status-structure
- name: Openapi Network Payload Structure
  property_count: 3
  slug: openapi-network-payload-structure
- name: Openapi Network Status Structure
  property_count: 4
  slug: openapi-network-status-structure
- name: Openapi Next Token Structure
  property_count: 0
  slug: openapi-next-token-structure
- name: Openapi Node Asset Name Structure
  property_count: 0
  slug: openapi-node-asset-name-structure
- name: Openapi Node Category Structure
  property_count: 0
  slug: openapi-node-category-structure
- name: Openapi Node From Template Job List Structure
  property_count: 0
  slug: openapi-node-from-template-job-list-structure
- name: Openapi Node From Template Job Status Message Structure
  property_count: 0
  slug: openapi-node-from-template-job-status-message-structure
- name: Openapi Node From Template Job Status Structure
  property_count: 0
  slug: openapi-node-from-template-job-status-structure
- name: Openapi Node From Template Job Structure
  property_count: 6
  slug: openapi-node-from-template-job-structure
- name: Openapi Node Id Structure
  property_count: 0
  slug: openapi-node-id-structure
- name: Openapi Node Input Port Structure
  property_count: 5
  slug: openapi-node-input-port-structure
- name: Openapi Node Instance Id Structure
  property_count: 0
  slug: openapi-node-instance-id-structure
- name: Openapi Node Instance Status Structure
  property_count: 0
  slug: openapi-node-instance-status-structure
- name: Openapi Node Instance Structure
  property_count: 7
  slug: openapi-node-instance-structure
- name: Openapi Node Instances Structure
  property_count: 0
  slug: openapi-node-instances-structure
- name: Openapi Node Interface Structure
  property_count: 2
  slug: openapi-node-interface-structure
- name: Openapi Node Name Structure
  property_count: 0
  slug: openapi-node-name-structure
- name: Openapi Node Output Port Structure
  property_count: 3
  slug: openapi-node-output-port-structure
- name: Openapi Node Package Arn Structure
  property_count: 0
  slug: openapi-node-package-arn-structure
- name: Openapi Node Package Id Structure
  property_count: 0
  slug: openapi-node-package-id-structure
- name: Openapi Node Package Name Structure
  property_count: 0
  slug: openapi-node-package-name-structure
- name: Openapi Node Package Patch Version Structure
  property_count: 0
  slug: openapi-node-package-patch-version-structure
- name: Openapi Node Package Version Structure
  property_count: 0
  slug: openapi-node-package-version-structure
- name: Openapi Node Signal List Structure
  property_count: 0
  slug: openapi-node-signal-list-structure
- name: Openapi Node Signal Structure
  property_count: 2
  slug: openapi-node-signal-structure
- name: Openapi Node Signal Value Structure
  property_count: 0
  slug: openapi-node-signal-value-structure
- name: Openapi Node Structure
  property_count: 11
  slug: openapi-node-structure
- name: Openapi Nodes List Structure
  property_count: 0
  slug: openapi-nodes-list-structure
- name: Openapi Ntp Payload Structure
  property_count: 1
  slug: openapi-ntp-payload-structure
- name: Openapi Ntp Server List Structure
  property_count: 0
  slug: openapi-ntp-server-list-structure
- name: Openapi Ntp Server Name Structure
  property_count: 0
  slug: openapi-ntp-server-name-structure
- name: Openapi Ntp Status Structure
  property_count: 3
  slug: openapi-ntp-status-structure
- name: Openapi Object Key Structure
  property_count: 0
  slug: openapi-object-key-structure
- name: Openapi Object Structure
  property_count: 0
  slug: openapi-object-structure
- name: Openapi Ota Job Config Structure
  property_count: 2
  slug: openapi-ota-job-config-structure
- name: Openapi Out Put S3 Location Structure
  property_count: 2
  slug: openapi-out-put-s3-location-structure
- name: Openapi Output Port List Structure
  property_count: 0
  slug: openapi-output-port-list-structure
- name: Openapi Package Import Job Input Config Structure
  property_count: 1
  slug: openapi-package-import-job-input-config-structure
- name: Openapi Package Import Job List Structure
  property_count: 0
  slug: openapi-package-import-job-list-structure
- name: Openapi Package Import Job Output Config Structure
  property_count: 1
  slug: openapi-package-import-job-output-config-structure
- name: Openapi Package Import Job Output Structure
  property_count: 4
  slug: openapi-package-import-job-output-structure
- name: Openapi Package Import Job Status Message Structure
  property_count: 0
  slug: openapi-package-import-job-status-message-structure
- name: Openapi Package Import Job Status Structure
  property_count: 0
  slug: openapi-package-import-job-status-structure
- name: Openapi Package Import Job Structure
  property_count: 6
  slug: openapi-package-import-job-structure
- name: Openapi Package Import Job Type Structure
  property_count: 0
  slug: openapi-package-import-job-type-structure
- name: Openapi Package List Item Structure
  property_count: 5
  slug: openapi-package-list-item-structure
- name: Openapi Package List Structure
  property_count: 0
  slug: openapi-package-list-structure
- name: Openapi Package Object Structure
  property_count: 3
  slug: openapi-package-object-structure
- name: Openapi Package Objects Structure
  property_count: 0
  slug: openapi-package-objects-structure
- name: Openapi Package Owner Account Structure
  property_count: 0
  slug: openapi-package-owner-account-structure
- name: Openapi Package Version Input Config Structure
  property_count: 1
  slug: openapi-package-version-input-config-structure
- name: Openapi Package Version Output Config Structure
  property_count: 3
  slug: openapi-package-version-output-config-structure
- name: Openapi Package Version Status Description Structure
  property_count: 0
  slug: openapi-package-version-status-description-structure
- name: Openapi Package Version Status Structure
  property_count: 0
  slug: openapi-package-version-status-structure
- name: Openapi Port Default Value Structure
  property_count: 0
  slug: openapi-port-default-value-structure
- name: Openapi Port Name Structure
  property_count: 0
  slug: openapi-port-name-structure
- name: Openapi Port Type Structure
  property_count: 0
  slug: openapi-port-type-structure
- name: Openapi Principal Arn Structure
  property_count: 0
  slug: openapi-principal-arn-structure
- name: Openapi Principal Arns List Structure
  property_count: 0
  slug: openapi-principal-arns-list-structure
- name: Openapi Provision Device Request Structure
  property_count: 4
  slug: openapi-provision-device-request-structure
- name: Openapi Provision Device Response Structure
  property_count: 5
  slug: openapi-provision-device-response-structure
- name: Openapi Region Structure
  property_count: 0
  slug: openapi-region-structure
- name: Openapi Register Package Version Request Structure
  property_count: 2
  slug: openapi-register-package-version-request-structure
- name: Openapi Register Package Version Response Structure
  property_count: 0
  slug: openapi-register-package-version-response-structure
- name: Openapi Remove Application Instance Request Structure
  property_count: 0
  slug: openapi-remove-application-instance-request-structure
- name: Openapi Remove Application Instance Response Structure
  property_count: 0
  slug: openapi-remove-application-instance-response-structure
- name: Openapi Reported Runtime Context State Structure
  property_count: 4
  slug: openapi-reported-runtime-context-state-structure
- name: Openapi Reported Runtime Context States Structure
  property_count: 0
  slug: openapi-reported-runtime-context-states-structure
- name: Openapi Resource Arn Structure
  property_count: 0
  slug: openapi-resource-arn-structure
- name: Openapi Resource Not Found Exception Structure
  property_count: 0
  slug: openapi-resource-not-found-exception-structure
- name: Openapi Runtime Context Name Structure
  property_count: 0
  slug: openapi-runtime-context-name-structure
- name: Openapi Runtime Role Arn Structure
  property_count: 0
  slug: openapi-runtime-role-arn-structure
- name: Openapi S3 Location Structure
  property_count: 3
  slug: openapi-s3-location-structure
- name: Openapi Service Quota Exceeded Exception Structure
  property_count: 0
  slug: openapi-service-quota-exceeded-exception-structure
- name: Openapi Signal Application Instance Node Instances Request Structure
  property_count: 1
  slug: openapi-signal-application-instance-node-instances-request-structure
- name: Openapi Signal Application Instance Node Instances Response Structure
  property_count: 1
  slug: openapi-signal-application-instance-node-instances-response-structure
- name: Openapi Sort Order Structure
  property_count: 0
  slug: openapi-sort-order-structure
- name: Openapi Static Ip Connection Info Structure
  property_count: 4
  slug: openapi-static-ip-connection-info-structure
- name: Openapi Status Filter Structure
  property_count: 0
  slug: openapi-status-filter-structure
- name: Openapi Storage Location Structure
  property_count: 5
  slug: openapi-storage-location-structure
- name: Openapi Tag Key List Structure
  property_count: 0
  slug: openapi-tag-key-list-structure
- name: Openapi Tag Key Structure
  property_count: 0
  slug: openapi-tag-key-structure
- name: Openapi Tag Map Structure
  property_count: 0
  slug: openapi-tag-map-structure
- name: Openapi Tag Resource Request Structure
  property_count: 1
  slug: openapi-tag-resource-request-structure
- name: Openapi Tag Resource Response Structure
  property_count: 0
  slug: openapi-tag-resource-response-structure
- name: Openapi Tag Value Structure
  property_count: 0
  slug: openapi-tag-value-structure
- name: Openapi Template Key Structure
  property_count: 0
  slug: openapi-template-key-structure
- name: Openapi Template Parameters Map Structure
  property_count: 0
  slug: openapi-template-parameters-map-structure
- name: Openapi Template Type Structure
  property_count: 0
  slug: openapi-template-type-structure
- name: Openapi Template Value Structure
  property_count: 0
  slug: openapi-template-value-structure
- name: Openapi Time Stamp Structure
  property_count: 0
  slug: openapi-time-stamp-structure
- name: Openapi Token Structure
  property_count: 0
  slug: openapi-token-structure
- name: Openapi Untag Resource Request Structure
  property_count: 0
  slug: openapi-untag-resource-request-structure
- name: Openapi Untag Resource Response Structure
  property_count: 0
  slug: openapi-untag-resource-response-structure
- name: Openapi Update Created Time Structure
  property_count: 0
  slug: openapi-update-created-time-structure
- name: Openapi Update Device Metadata Request Structure
  property_count: 1
  slug: openapi-update-device-metadata-request-structure
- name: Openapi Update Device Metadata Response Structure
  property_count: 1
  slug: openapi-update-device-metadata-response-structure
- name: Openapi Update Progress Structure
  property_count: 0
  slug: openapi-update-progress-structure
- name: Openapi Validation Exception Structure
  property_count: 0
  slug: openapi-validation-exception-structure
- name: Openapi Version Structure
  property_count: 0
  slug: openapi-version-structure
jsonld:
- class_count: 169
  name: Amazon Panorama Openapi Context
  property_count: 127
  slug: amazon-panorama-openapi-context
layout: provider
modified: '2026-05-19'
name: Amazon Panorama
nav: Providers
network: true
overview: 'Amazon Panorama publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Application Instances API, Devices API, Jobs API, and 3 more. Tagged areas include Cameras, Computer Vision, Edge ML, and Industrial IoT.


  The Amazon Panorama catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Panorama''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 20 more developer resources.'
plans:
- name: Amazon Panorama Plans Pricing
  plan_count: 3
  slug: amazon-panorama-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Amazon Panorama Rate Limits
  slug: amazon-panorama-rate-limits
rules:
- name: Amazon Panorama API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-panorama-jsonschema-spectral-rules
- name: Amazon Panorama API Rules
  rule_count: 26
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 15
  slug: amazon-panorama-spectral-rules
score:
  band: strong
  composite: 57.2
  delta: -8.5
  facets:
    commercial_clarity: 57.9
    contract_quality: 71.9
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-panorama/refs/heads/main/screenshots/amazon-panorama-2026-06-20T171756.png
security:
- kind: authentication
  name: Amazon Panorama Authentication
  slug: amazon-panorama-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Panorama Domain Security
  slug: amazon-panorama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Panorama Vulnerability Disclosure
  slug: amazon-panorama-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Panorama Trust Center
  slug: amazon-panorama-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-panorama
tags:
- Cameras
- Computer Vision
- Edge ML
- Industrial IoT
website: https://aws.amazon.com/panorama/
---
