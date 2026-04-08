---
aid: amazon-elastic-load-balancing
url: https://raw.githubusercontent.com/api-evangelist/amazon-elastic-load-balancing/refs/heads/main/apis.yml
apis:
- name: Elastic Load Balancing v2 API
  description: API for managing Application Load Balancers (ALB), Network Load Balancers (NLB), and Gateway Load Balancers (GLB). Provides advanced routing, target group management, listener configuration, and rule-based traffic distribution across multiple targets.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/elasticloadbalancing/
  baseURL: https://elasticloadbalancing.amazonaws.com
  tags:
  - ALB
  - GLB
  - Load Balancing
  - Networking
  - NLB
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/
  - type: OpenAPI
    url: openapi/amazon-elastic-load-balancing-openapi.yml
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticloadbalancingv2/2015-12-01/openapi.yaml
  - type: JSONSchema
    url: json-schema/amazon-elastic-load-balancing-schema.json
  - type: JSONLD
    url: json-ld/amazon-elastic-load-balancing-context.jsonld
  - type: Pricing
    url: https://aws.amazon.com/elasticloadbalancing/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/elasticloadbalancing/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/elasticloadbalancing/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/
  - type: API Reference
    url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/elbv2/
  - type: Security
    url: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/security.html
- name: Classic Load Balancing API
  description: API for managing Classic Load Balancers, which provide basic load balancing across multiple Amazon EC2 instances at the request level and the connection level. Classic Load Balancers are intended for applications built within the EC2-Classic network.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  humanURL: https://aws.amazon.com/elasticloadbalancing/
  baseURL: https://elasticloadbalancing.amazonaws.com
  tags:
  - Classic
  - Load Balancing
  - Networking
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticloadbalancing/2012-06-01/openapi.yaml
  - type: Pricing
    url: https://aws.amazon.com/elasticloadbalancing/pricing/
  - type: Getting Started
    url: https://aws.amazon.com/elasticloadbalancing/getting-started/
  - type: FAQ
    url: https://aws.amazon.com/elasticloadbalancing/faqs/
  - type: User Guide
    url: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/
  - type: API Reference
    url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/
  - type: CLI Reference
    url: https://docs.aws.amazon.com/cli/latest/reference/elb/
  - type: Security
    url: https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/security.html
name: Amazon Elastic Load Balancing
tags:
- AWS
- High Availability
- Load Balancing
- Networking
- Scalability
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Elastic Load Balancing automatically distributes incoming application traffic across multiple targets, such as Amazon EC2 instances, containers, IP addresses, and Lambda functions, ensuring high availability and fault tolerance for your applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

