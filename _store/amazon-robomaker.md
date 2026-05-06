---
name: Amazon RoboMaker
description: AWS RoboMaker is a cloud-based service that makes it easy to develop, simulate, and deploy intelligent robotics applications. RoboMaker extends the most widely used open-source robotics software framework, Robot Operating System (ROS), with connectivity to cloud services, providing tools for building, testing, and deploying robotics applications at scale.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-robomaker/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: AWS RoboMaker API
    description: The AWS RoboMaker API provides programmatic access to create and manage robotics applications, simulation jobs, and fleet deployments. It enables developers to build robot applications, run simulation jobs for testing, manage simulation worlds, and deploy applications to physical robots at scale.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/robomaker/
    baseURL: https://robomaker.amazonaws.com
    tags:
      - AWS
      - Robotics
      - Simulation
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/robomaker/
      - type: OpenAPI
        url: openapi/amazon-robomaker-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/robomaker/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/robomaker/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/robomaker/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/robomaker/
  - type: Documentation
    url: https://docs.aws.amazon.com/robomaker/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Portal
    url: https://console.aws.amazon.com/robomaker/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: JSON-LD
    url: json-ld/amazon-robomaker-context-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-architecture-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-arn-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-arns-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-batch-delete-worlds-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-batch-delete-worlds-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-batch-describe-simulation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-batch-describe-simulation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-batch-policy-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-batch-timeout-in-seconds-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-boolean-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-boxed-boolean-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-deployment-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-deployment-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-simulation-job-batch-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-simulation-job-batch-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-simulation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-simulation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-world-export-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-world-export-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-world-generation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-cancel-world-generation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-client-request-token-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-command-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-command-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-compute-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-compute-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-compute-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-concurrent-deployment-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-deployment-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-deployment-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-fleet-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-fleet-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-robot-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-robot-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-robot-application-version-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-robot-application-version-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-robot-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-robot-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-simulation-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-simulation-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-simulation-application-version-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-simulation-application-version-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-simulation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-simulation-job-requests-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-simulation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-world-export-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-world-export-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-world-generation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-world-generation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-world-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-create-world-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-created-at-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-data-source-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-data-source-configs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-data-source-names-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-data-source-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-data-source-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-data-sources-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-fleet-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-fleet-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-robot-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-robot-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-robot-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-robot-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-simulation-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-simulation-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-world-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-delete-world-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-application-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-application-configs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-job-error-code-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-job-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-jobs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-launch-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-timeout-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deployment-version-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deregister-robot-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-deregister-robot-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-deployment-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-deployment-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-fleet-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-fleet-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-robot-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-robot-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-robot-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-robot-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-simulation-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-simulation-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-simulation-job-batch-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-simulation-job-batch-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-simulation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-simulation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-export-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-export-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-generation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-generation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-describe-world-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-environment-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-environment-variable-key-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-environment-variable-map-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-environment-variable-value-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-exit-behavior-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-failed-at-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-failed-create-simulation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-failed-create-simulation-job-requests-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-failure-behavior-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-failure-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-filter-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-filter-values-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-filters-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-finished-worlds-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-fleet-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-fleets-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-floorplan-count-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-generic-integer-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-generic-string-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-get-world-template-body-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-get-world-template-body-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-gpu-unit-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-iam-role-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-idempotent-parameter-mismatch-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-image-digest-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-integer-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-interior-count-per-floorplan-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-internal-server-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-invalid-parameter-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-job-duration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-json-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-last-started-at-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-last-updated-at-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-launch-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-limit-exceeded-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-deployment-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-deployment-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-fleets-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-fleets-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-robot-applications-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-robot-applications-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-robots-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-robots-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-simulation-applications-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-simulation-applications-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-simulation-job-batches-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-simulation-job-batches-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-simulation-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-simulation-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-tags-for-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-tags-for-resource-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-world-export-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-world-export-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-world-generation-jobs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-world-generation-jobs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-world-templates-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-world-templates-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-worlds-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-list-worlds-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-logging-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-max-concurrency-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-max-results-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-network-interface-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-non-empty-string-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-non-system-port-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-output-location-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-pagination-token-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-path-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-percent-done-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-percentage-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-port-forwarding-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-port-mapping-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-port-mapping-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-port-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-progress-detail-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-register-robot-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-register-robot-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-rendering-engine-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-rendering-engine-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-rendering-engine-version-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-repository-url-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-resource-already-exists-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-resource-not-found-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-restart-simulation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-restart-simulation-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-revision-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-application-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-application-configs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-application-names-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-application-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-application-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-deployment-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-deployment-step-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-deployment-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-software-suite-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-software-suite-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-software-suite-version-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robot-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-robots-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-bucket-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-etag-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-etags-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-key-or-prefix-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-key-output-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-key-outputs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-key-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-keys-or-prefixes-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-s3-object-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-security-groups-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-service-unavailable-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-application-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-application-configs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-application-names-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-application-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-application-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-batch-error-code-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-batch-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-batch-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-batch-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-error-code-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-job-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-jobs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-software-suite-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-software-suite-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-software-suite-version-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-time-millis-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-simulation-unit-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-source-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-source-configs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-source-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-sources-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-start-simulation-job-batch-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-start-simulation-job-batch-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-subnets-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-sync-deployment-job-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-sync-deployment-job-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tag-key-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tag-key-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tag-map-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tag-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tag-resource-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tag-value-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-template-location-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-template-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-template-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-template-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-throttling-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tool-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-tools-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-unrestricted-command-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-untag-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-untag-resource-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-update-robot-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-update-robot-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-update-simulation-application-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-update-simulation-application-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-update-world-template-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-update-world-template-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-upload-behavior-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-upload-configuration-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-upload-configurations-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-version-qualifier-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-version-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-vpc-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-vpc-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-configs-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-count-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-export-job-error-code-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-export-job-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-export-job-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-export-job-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-failure-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-failures-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-generation-job-error-code-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-generation-job-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-generation-job-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-generation-job-summary-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-summaries-schema.json
  - type: JSONSchema
    url: json-schema/amazon-robomaker-openapi-world-summary-schema.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-architecture-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-arn-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-arns-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-batch-delete-worlds-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-batch-delete-worlds-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-batch-describe-simulation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-batch-describe-simulation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-batch-policy-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-batch-timeout-in-seconds-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-boolean-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-boxed-boolean-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-deployment-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-deployment-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-simulation-job-batch-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-simulation-job-batch-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-simulation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-simulation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-world-export-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-world-export-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-world-generation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-cancel-world-generation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-client-request-token-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-command-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-command-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-compute-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-compute-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-compute-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-concurrent-deployment-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-deployment-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-deployment-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-fleet-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-fleet-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-robot-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-robot-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-robot-application-version-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-robot-application-version-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-robot-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-robot-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-simulation-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-simulation-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-simulation-application-version-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-simulation-application-version-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-simulation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-simulation-job-requests-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-simulation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-world-export-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-world-export-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-world-generation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-world-generation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-world-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-create-world-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-created-at-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-data-source-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-data-source-configs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-data-source-names-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-data-source-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-data-source-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-data-sources-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-fleet-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-fleet-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-robot-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-robot-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-robot-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-robot-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-simulation-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-simulation-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-world-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-delete-world-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-application-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-application-configs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-job-error-code-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-job-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-jobs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-launch-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-timeout-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deployment-version-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deregister-robot-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-deregister-robot-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-deployment-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-deployment-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-fleet-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-fleet-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-robot-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-robot-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-robot-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-robot-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-simulation-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-simulation-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-simulation-job-batch-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-simulation-job-batch-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-simulation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-simulation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-export-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-export-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-generation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-generation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-describe-world-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-environment-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-environment-variable-key-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-environment-variable-map-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-environment-variable-value-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-exit-behavior-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-failed-at-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-failed-create-simulation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-failed-create-simulation-job-requests-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-failure-behavior-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-failure-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-filter-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-filter-values-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-filters-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-finished-worlds-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-fleet-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-fleets-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-floorplan-count-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-generic-integer-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-generic-string-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-get-world-template-body-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-get-world-template-body-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-gpu-unit-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-iam-role-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-idempotent-parameter-mismatch-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-image-digest-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-integer-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-interior-count-per-floorplan-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-internal-server-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-invalid-parameter-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-job-duration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-json-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-last-started-at-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-last-updated-at-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-launch-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-limit-exceeded-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-deployment-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-deployment-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-fleets-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-fleets-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-robot-applications-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-robot-applications-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-robots-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-robots-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-simulation-applications-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-simulation-applications-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-simulation-job-batches-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-simulation-job-batches-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-simulation-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-simulation-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-tags-for-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-tags-for-resource-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-world-export-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-world-export-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-world-generation-jobs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-world-generation-jobs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-world-templates-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-world-templates-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-worlds-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-list-worlds-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-logging-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-max-concurrency-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-max-results-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-network-interface-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-non-empty-string-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-non-system-port-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-output-location-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-pagination-token-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-path-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-percent-done-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-percentage-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-port-forwarding-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-port-mapping-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-port-mapping-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-port-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-progress-detail-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-register-robot-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-register-robot-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-rendering-engine-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-rendering-engine-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-rendering-engine-version-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-repository-url-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-resource-already-exists-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-resource-not-found-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-restart-simulation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-restart-simulation-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-revision-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-application-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-application-configs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-application-names-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-application-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-application-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-deployment-step-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-deployment-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-deployment-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-software-suite-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-software-suite-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-software-suite-version-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robot-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-robots-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-bucket-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-etag-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-etags-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-key-or-prefix-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-key-output-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-key-outputs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-key-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-keys-or-prefixes-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-s3-object-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-security-groups-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-service-unavailable-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-application-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-application-configs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-application-names-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-application-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-application-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-batch-error-code-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-batch-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-batch-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-batch-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-error-code-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-job-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-jobs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-software-suite-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-software-suite-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-software-suite-version-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-time-millis-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-simulation-unit-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-source-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-source-configs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-source-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-sources-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-start-simulation-job-batch-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-start-simulation-job-batch-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-subnets-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-sync-deployment-job-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-sync-deployment-job-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tag-key-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tag-key-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tag-map-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tag-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tag-resource-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tag-value-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-template-location-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-template-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-template-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-template-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-throttling-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tool-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-tools-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-unrestricted-command-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-untag-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-untag-resource-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-update-robot-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-update-robot-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-update-simulation-application-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-update-simulation-application-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-update-world-template-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-update-world-template-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-upload-behavior-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-upload-configuration-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-upload-configurations-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-version-qualifier-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-version-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-vpc-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-vpc-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-configs-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-count-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-export-job-error-code-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-export-job-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-export-job-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-export-job-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-failure-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-failures-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-generation-job-error-code-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-generation-job-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-generation-job-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-generation-job-summary-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-summaries-structure.json
  - type: JSONStructure
    url: json-structure/amazon-robomaker-openapi-world-summary-structure.json
  - type: Example
    url: examples/amazon-robomaker-openapi-batch-delete-worlds-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-batch-delete-worlds-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-batch-describe-simulation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-batch-describe-simulation-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-batch-policy-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-cancel-deployment-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-cancel-simulation-job-batch-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-cancel-simulation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-cancel-world-export-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-cancel-world-generation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-compute-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-compute-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-deployment-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-deployment-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-fleet-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-fleet-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-robot-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-robot-application-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-robot-application-version-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-robot-application-version-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-robot-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-robot-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-simulation-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-simulation-application-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-simulation-application-version-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-simulation-application-version-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-simulation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-simulation-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-world-export-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-world-export-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-world-generation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-world-generation-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-world-template-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-create-world-template-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-data-source-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-data-source-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-delete-fleet-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-delete-robot-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-delete-robot-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-delete-simulation-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-delete-world-template-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-deployment-application-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-deployment-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-deployment-job-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-deployment-launch-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-deregister-robot-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-deregister-robot-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-deployment-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-deployment-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-fleet-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-fleet-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-robot-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-robot-application-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-robot-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-robot-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-simulation-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-simulation-application-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-simulation-job-batch-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-simulation-job-batch-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-simulation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-simulation-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-export-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-export-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-generation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-generation-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-template-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-describe-world-template-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-environment-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-failed-create-simulation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-failure-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-filter-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-finished-worlds-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-fleet-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-get-world-template-body-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-get-world-template-body-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-launch-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-deployment-jobs-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-deployment-jobs-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-fleets-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-fleets-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-robot-applications-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-robot-applications-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-robots-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-robots-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-simulation-applications-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-simulation-applications-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-simulation-job-batches-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-simulation-job-batches-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-simulation-jobs-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-simulation-jobs-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-tags-for-resource-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-world-export-jobs-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-world-export-jobs-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-world-generation-jobs-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-world-generation-jobs-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-world-templates-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-world-templates-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-worlds-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-list-worlds-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-logging-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-network-interface-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-output-location-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-port-forwarding-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-port-mapping-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-progress-detail-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-register-robot-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-register-robot-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-rendering-engine-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-restart-simulation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-robot-application-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-robot-application-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-robot-deployment-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-robot-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-robot-software-suite-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-s3-key-output-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-s3-object-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-simulation-application-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-simulation-application-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-simulation-job-batch-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-simulation-job-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-simulation-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-simulation-job-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-simulation-software-suite-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-source-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-source-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-start-simulation-job-batch-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-start-simulation-job-batch-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-sync-deployment-job-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-sync-deployment-job-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-tag-resource-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-template-location-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-template-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-tool-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-update-robot-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-update-robot-application-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-update-simulation-application-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-update-simulation-application-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-update-world-template-request-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-update-world-template-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-upload-configuration-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-vpc-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-vpc-config-response-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-world-config-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-world-count-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-world-export-job-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-world-failure-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-world-generation-job-summary-example.json
  - type: Example
    url: examples/amazon-robomaker-openapi-world-summary-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-robomaker.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-robomaker.yaml
  - type: SpectralRules
    url: rules/amazon-robomaker-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-robomaker-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - Robotics
  - Simulation
---
