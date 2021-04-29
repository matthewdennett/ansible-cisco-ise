# Ansible Collection - cisco.ise

## Ansible Modules for Cisco ISE

The <tbd> project provides an Ansible collection for managing and automating your Cisco ISE environment. It consists of a set of modules and roles for performing tasks related to Cisco ISE.

This collection has been tested and supports Cisco ISE 3.0.

*Note: This collection is not compatible with versions of Ansible before v2.9.*

## Requirements
- Ansible >= 2.9
- [Cisco ISE SDK](https://github.com/<tbd>/<tbd>) v2.1.1 or newer
- Python >= 3.5, as the Cisco ISE SDK doesn't support Python version 2.x

## Install
Ansible must be installed
```
sudo pip install ansible
```

Cisco ISE SDK must be installed
```
sudo pip install isesdk
```

Install the collection
```
ansible-galaxy collection install cisco.ise
```
## Use
First, define a `credentials.yml` file where you specify your Cisco ISE credentials as ansible variables:
```
---
ise_hostname: <A.B.C.D>
ise_username: <username>
ise_password: <password>
ise_version: 3.1.0  # optional, defaults to 3.0.0
ise_verify: False  # optional, defaults to True
```

Then, create a playbook `myplaybook.yml` referencing the variables in your credentials.yml file and specifying the full namespace path to the module, plugin and/or role:
```
- hosts: ise_servers
  vars_files:
    - credentials.yml
  gather_facts: no
  tasks:
  - name: Get network device by id
    cisco.ise.network_device_info:
      ise_hostname: "{{ise_host}}"
      ise_username: "{{ise_username}}"
      ise_password: "{{ise_password}}"
      ise_verify: "{{ise_verify}}"
      id: "0667bc80-78a9-11eb-b987-005056aba98b"
```

Execute the playbook:
```
ansible-playbook -i hosts myplaybook.yml
```
In the `playbooks` directory you can find more examples and use cases.


## Update
Getting the latest/nightly collection build

Clone the <tbd> repository.
```
git clone https://github.com/<tbd>/<tbd>.git
```

Go to the <tbd> directory
```
cd <tbd>
```

Pull the latest master from the repo
```
git pull origin master
```

Build and install a collection from source
```
ansible-galaxy collection build --force
ansible-galaxy collection install cisco-ise-* --force
```

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Attention macOS users

If you're using macOS you may receive this error when running your playbook:

```
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called.
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
ERROR! A worker was found in a dead state
```

If that's the case try setting this environment variable:
```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

## Contributing to this collection

Ongoing development efforts and contributions to this collection are tracked as issues in this repository.

We welcome community contributions to this collection. If you find problems, need an enhancement or need a new module, please open an issue or create a PR against the [Cisco ISE Ansible collection repository](https://github.com/<tbd>/<tbd>/issues).

## Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Releasing, Versioning and Deprecation

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

New minor and major releases as well as deprecations will follow new releases and deprecations of the Cisco ISE product, its REST API and the corresponding Python SDK, which this project relies on. 
