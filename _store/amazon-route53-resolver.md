---
name: Amazon Route 53 Resolver
description: Amazon Route 53 Resolver provides DNS resolution for hybrid cloud environments, enabling DNS queries between your VPCs and on-premises networks. It allows you to configure DNS forwarding rules, manage resolver endpoints, and set up conditional forwarding to resolve domain names across your hybrid infrastructure seamlessly.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://raw.githubusercontent.com/api-evangelist/amazon-route53-resolver/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
apis:
  - name: Amazon Route 53 Resolver API
    description: The Amazon Route 53 Resolver API provides programmatic access to manage DNS resolution across hybrid cloud environments. It enables developers to create and manage resolver endpoints, configure forwarding rules, associate VPCs with resolver rules, and manage DNS firewall rule groups for filtering DNS queries.
    image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
    humanURL: https://aws.amazon.com/route53/
    baseURL: https://route53resolver.amazonaws.com
    tags:
      - AWS
      - DNS
      - Hybrid Cloud
      - Networking
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html
      - type: OpenAPI
        url: openapi/amazon-route53-resolver-openapi.yml
      - type: Pricing
        url: https://aws.amazon.com/route53/pricing/
      - type: GettingStarted
        url: https://aws.amazon.com/route53/getting-started/
      - type: FAQ
        url: https://aws.amazon.com/route53/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: Portal
    url: https://aws.amazon.com/route53/
  - type: Documentation
    url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Portal
    url: https://console.aws.amazon.com/route53resolver/
  - type: SignUp
    url: https://signin.aws.amazon.com/signup?request_type=register
  - type: Login
    url: https://aws.amazon.com/console/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: JSON-LD
    url: json-ld/amazon-route53-resolver-context-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-access-denied-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-account-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-action-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-arn-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-firewall-rule-group-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-firewall-rule-group-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-resolver-endpoint-ip-address-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-resolver-endpoint-ip-address-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-resolver-query-log-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-resolver-query-log-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-resolver-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-associate-resolver-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-autodefined-reverse-flag-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-block-override-dns-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-block-override-domain-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-block-override-ttl-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-block-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-boolean-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-conflict-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-count-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-firewall-domain-list-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-firewall-domain-list-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-firewall-rule-group-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-firewall-rule-group-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-firewall-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-firewall-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-resolver-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-resolver-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-resolver-query-log-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-resolver-query-log-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-resolver-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-create-resolver-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-creator-request-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-firewall-domain-list-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-firewall-domain-list-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-firewall-rule-group-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-firewall-rule-group-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-firewall-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-firewall-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-resolver-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-resolver-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-resolver-query-log-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-resolver-query-log-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-resolver-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-delete-resolver-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-destination-arn-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-firewall-rule-group-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-firewall-rule-group-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-resolver-endpoint-ip-address-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-resolver-endpoint-ip-address-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-resolver-query-log-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-resolver-query-log-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-resolver-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-disassociate-resolver-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-domain-list-file-url-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-domain-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-filter-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-filter-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-filter-value-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-filter-values-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-filters-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-config-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domain-import-operation-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domain-list-metadata-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domain-list-metadata-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domain-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domain-list-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domain-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domain-update-operation-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-domains-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-fail-open-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-association-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-association-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-associations-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-metadata-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-metadata-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-policy-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-group-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rule-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-firewall-rules-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-domain-list-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-domain-list-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-rule-group-association-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-rule-group-association-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-rule-group-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-rule-group-policy-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-rule-group-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-firewall-rule-group-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-dnssec-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-dnssec-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-query-log-config-association-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-query-log-config-association-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-query-log-config-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-query-log-config-policy-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-query-log-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-query-log-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-rule-association-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-rule-association-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-rule-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-rule-policy-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-get-resolver-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-import-firewall-domains-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-import-firewall-domains-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-internal-service-error-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-invalid-next-token-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-invalid-parameter-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-invalid-policy-document-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-invalid-request-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-invalid-tag-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-address-count-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-address-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-address-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-address-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-address-update-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-addresses-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-addresses-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ip-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-ipv6-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-limit-exceeded-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-domain-max-results-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-configs-max-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-configs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-configs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-domain-lists-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-domain-lists-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-domains-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-domains-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-rule-group-associations-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-rule-group-associations-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-rule-groups-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-rule-groups-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-rules-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-firewall-rules-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-configs-max-result-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-configs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-configs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-dnssec-configs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-dnssec-configs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-endpoint-ip-addresses-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-endpoint-ip-addresses-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-endpoints-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-endpoints-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-query-log-config-associations-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-query-log-config-associations-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-query-log-configs-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-query-log-configs-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-rule-associations-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-rule-associations-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-rules-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-resolver-rules-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-tags-for-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-list-tags-for-resource-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-max-results-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-mutation-protection-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-next-token-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-port-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-priority-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-put-firewall-rule-group-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-put-firewall-rule-group-policy-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-put-resolver-query-log-config-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-put-resolver-query-log-config-policy-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-put-resolver-rule-policy-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-put-resolver-rule-policy-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-autodefined-reverse-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-config-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-dnssec-config-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-dnssec-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-dnssec-validation-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-endpoint-direction-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-endpoint-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-endpoint-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-endpoint-type-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-endpoints-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-association-error-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-association-error-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-association-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-association-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-association-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-name-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-policy-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-query-log-config-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rule-association-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rule-association-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rule-associations-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rule-config-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rule-policy-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rule-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rule-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resolver-rules-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resource-exists-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resource-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resource-in-use-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resource-not-found-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-resource-unavailable-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-rfc3339-time-string-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-rule-type-option-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-security-group-ids-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-service-principle-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-share-status-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-sort-by-key-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-sort-order-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-status-message-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-subnet-id-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-tag-key-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-tag-key-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-tag-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-tag-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-tag-resource-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-tag-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-tag-value-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-target-address-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-target-list-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-throttling-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-unknown-resource-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-unsigned-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-untag-resource-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-untag-resource-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-domains-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-domains-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-rule-group-association-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-rule-group-association-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-firewall-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-ip-address-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-ip-addresses-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-dnssec-config-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-dnssec-config-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-endpoint-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-endpoint-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-rule-request-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-update-resolver-rule-response-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-validation-exception-schema.json
  - type: JSONSchema
    url: json-schema/amazon-route53-resolver-openapi-validation-schema.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-access-denied-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-account-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-action-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-arn-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-firewall-rule-group-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-firewall-rule-group-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-resolver-endpoint-ip-address-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-resolver-endpoint-ip-address-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-resolver-query-log-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-resolver-query-log-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-resolver-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-associate-resolver-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-autodefined-reverse-flag-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-block-override-dns-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-block-override-domain-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-block-override-ttl-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-block-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-boolean-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-conflict-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-count-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-firewall-domain-list-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-firewall-domain-list-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-firewall-rule-group-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-firewall-rule-group-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-firewall-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-firewall-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-resolver-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-resolver-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-resolver-query-log-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-resolver-query-log-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-resolver-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-create-resolver-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-creator-request-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-firewall-domain-list-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-firewall-domain-list-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-firewall-rule-group-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-firewall-rule-group-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-firewall-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-firewall-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-resolver-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-resolver-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-resolver-query-log-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-resolver-query-log-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-resolver-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-delete-resolver-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-destination-arn-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-firewall-rule-group-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-firewall-rule-group-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-resolver-endpoint-ip-address-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-resolver-endpoint-ip-address-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-resolver-query-log-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-resolver-query-log-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-resolver-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-disassociate-resolver-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-domain-list-file-url-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-domain-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-filter-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-filter-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-filter-value-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-filter-values-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-filters-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-config-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domain-import-operation-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domain-list-metadata-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domain-list-metadata-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domain-list-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domain-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domain-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domain-update-operation-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-domains-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-fail-open-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-association-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-association-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-associations-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-metadata-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-metadata-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-policy-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-group-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rule-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-firewall-rules-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-domain-list-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-domain-list-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-rule-group-association-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-rule-group-association-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-rule-group-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-rule-group-policy-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-rule-group-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-firewall-rule-group-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-dnssec-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-dnssec-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-query-log-config-association-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-query-log-config-association-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-query-log-config-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-query-log-config-policy-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-query-log-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-query-log-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-rule-association-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-rule-association-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-rule-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-rule-policy-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-get-resolver-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-import-firewall-domains-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-import-firewall-domains-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-internal-service-error-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-invalid-next-token-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-invalid-parameter-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-invalid-policy-document-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-invalid-request-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-invalid-tag-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-address-count-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-address-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-address-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-address-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-address-update-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-addresses-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-addresses-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ip-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-ipv6-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-limit-exceeded-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-domain-max-results-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-configs-max-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-configs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-configs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-domain-lists-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-domain-lists-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-domains-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-domains-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-rule-group-associations-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-rule-group-associations-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-rule-groups-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-rule-groups-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-rules-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-firewall-rules-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-configs-max-result-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-configs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-configs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-dnssec-configs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-dnssec-configs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-endpoint-ip-addresses-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-endpoint-ip-addresses-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-endpoints-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-endpoints-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-query-log-config-associations-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-query-log-config-associations-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-query-log-configs-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-query-log-configs-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-rule-associations-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-rule-associations-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-rules-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-resolver-rules-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-tags-for-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-list-tags-for-resource-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-max-results-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-mutation-protection-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-next-token-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-port-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-priority-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-put-firewall-rule-group-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-put-firewall-rule-group-policy-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-put-resolver-query-log-config-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-put-resolver-query-log-config-policy-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-put-resolver-rule-policy-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-put-resolver-rule-policy-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-autodefined-reverse-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-config-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-dnssec-config-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-dnssec-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-dnssec-validation-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-endpoint-direction-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-endpoint-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-endpoint-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-endpoint-type-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-endpoints-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-association-error-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-association-error-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-association-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-association-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-association-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-name-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-policy-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-query-log-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rule-association-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rule-association-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rule-associations-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rule-config-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rule-policy-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rule-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rule-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resolver-rules-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resource-exists-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resource-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resource-in-use-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resource-not-found-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-resource-unavailable-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-rfc3339-time-string-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-rule-type-option-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-security-group-ids-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-service-principle-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-share-status-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-sort-by-key-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-sort-order-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-status-message-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-subnet-id-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-tag-key-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-tag-key-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-tag-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-tag-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-tag-resource-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-tag-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-tag-value-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-target-address-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-target-list-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-throttling-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-unknown-resource-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-unsigned-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-untag-resource-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-untag-resource-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-domains-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-domains-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-rule-group-association-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-rule-group-association-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-firewall-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-ip-address-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-ip-addresses-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-dnssec-config-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-dnssec-config-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-endpoint-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-endpoint-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-rule-request-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-update-resolver-rule-response-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-validation-exception-structure.json
  - type: JSONStructure
    url: json-structure/amazon-route53-resolver-openapi-validation-structure.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-firewall-rule-group-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-firewall-rule-group-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-resolver-endpoint-ip-address-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-resolver-endpoint-ip-address-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-resolver-query-log-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-resolver-query-log-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-resolver-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-associate-resolver-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-firewall-domain-list-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-firewall-domain-list-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-firewall-rule-group-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-firewall-rule-group-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-firewall-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-firewall-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-resolver-endpoint-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-resolver-endpoint-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-resolver-query-log-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-resolver-query-log-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-resolver-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-create-resolver-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-firewall-domain-list-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-firewall-domain-list-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-firewall-rule-group-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-firewall-rule-group-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-firewall-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-firewall-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-resolver-endpoint-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-resolver-endpoint-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-resolver-query-log-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-resolver-query-log-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-resolver-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-delete-resolver-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-firewall-rule-group-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-firewall-rule-group-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-resolver-endpoint-ip-address-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-resolver-endpoint-ip-address-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-resolver-query-log-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-resolver-query-log-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-resolver-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-disassociate-resolver-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-filter-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-firewall-config-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-firewall-domain-list-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-firewall-domain-list-metadata-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-firewall-rule-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-firewall-rule-group-association-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-firewall-rule-group-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-firewall-rule-group-metadata-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-domain-list-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-domain-list-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-rule-group-association-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-rule-group-association-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-rule-group-policy-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-rule-group-policy-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-rule-group-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-firewall-rule-group-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-dnssec-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-dnssec-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-endpoint-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-endpoint-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-query-log-config-association-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-query-log-config-association-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-query-log-config-policy-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-query-log-config-policy-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-query-log-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-query-log-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-rule-association-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-rule-association-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-rule-policy-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-rule-policy-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-get-resolver-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-import-firewall-domains-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-import-firewall-domains-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-ip-address-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-ip-address-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-ip-address-update-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-configs-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-configs-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-domain-lists-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-domain-lists-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-domains-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-domains-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-rule-group-associations-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-rule-group-associations-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-rule-groups-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-rule-groups-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-rules-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-firewall-rules-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-configs-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-configs-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-dnssec-configs-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-dnssec-configs-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-endpoint-ip-addresses-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-endpoint-ip-addresses-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-endpoints-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-endpoints-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-query-log-config-associations-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-query-log-config-associations-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-query-log-configs-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-query-log-configs-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-rule-associations-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-rule-associations-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-rules-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-resolver-rules-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-tags-for-resource-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-list-tags-for-resource-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-put-firewall-rule-group-policy-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-put-firewall-rule-group-policy-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-put-resolver-query-log-config-policy-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-put-resolver-query-log-config-policy-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-put-resolver-rule-policy-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-put-resolver-rule-policy-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-config-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-dnssec-config-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-endpoint-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-query-log-config-association-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-query-log-config-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-rule-association-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-rule-config-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-resolver-rule-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-tag-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-tag-resource-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-target-address-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-untag-resource-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-domains-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-domains-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-rule-group-association-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-rule-group-association-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-firewall-rule-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-ip-address-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-dnssec-config-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-dnssec-config-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-endpoint-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-endpoint-response-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-rule-request-example.json
  - type: Example
    url: examples/amazon-route53-resolver-openapi-update-resolver-rule-response-example.json
  - type: NaftikoCapability
    url: capabilities/amazon-route53-resolver.yaml
  - type: NaftikoCapability
    url: capabilities/shared/amazon-route53-resolver.yaml
  - type: SpectralRules
    url: rules/amazon-route53-resolver-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-route53-resolver-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AWS
  - DNS
  - Hybrid Cloud
  - Networking
---
