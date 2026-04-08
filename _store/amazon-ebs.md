---
aid: amazon-ebs
url: https://raw.githubusercontent.com/api-evangelist/amazon-ebs/refs/heads/main/apis.yml
apis:
- name: Amazon EBS API
  description: API for managing Amazon EBS volumes, snapshots, and related resources through the EC2 API.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  url: https://aws.amazon.com/ebs/
  baseURL: https://ec2.amazonaws.com
  properties:
  - type: documentation
    url: https://docs.aws.amazon.com/ebs/latest/userguide/
  - type: openapi
    url: openapi/amazon-ebs-openapi.yml
  - type: json-schema
    url: json-schema/amazon-ebs-volume-schema.json
  - type: json-ld
    url: json-ld/amazon-ebs-context.jsonld
  - type: pricing
    url: https://aws.amazon.com/ebs/pricing/
  - type: getting-started
    url: https://aws.amazon.com/ebs/getting-started/
  - type: faq
    url: https://aws.amazon.com/ebs/faqs/
  - type: user-guide
    url: https://docs.aws.amazon.com/ebs/latest/userguide/
  - type: api-reference
    url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/
  - type: cli-reference
    url: https://docs.aws.amazon.com/cli/latest/reference/ec2/
  - type: security
    url: https://docs.aws.amazon.com/ebs/latest/userguide/security.html
name: Amazon EBS
tags:
- Amazon Web Services
- AWS
- Block Storage
- EBS
- EC2
- Snapshots
- Storage
- Volumes
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon Elastic Block Store (EBS) provides persistent block storage volumes for use with Amazon EC2 instances. EBS volumes are highly available and reliable storage volumes that can be attached to any running instance in the same Availability Zone, offering consistent and low-latency performance for workloads that require persistent storage.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

