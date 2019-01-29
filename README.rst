Durex
=====

AWS Security Tool to improve security, performance and reduce costs based on [Awspice](https://github.com/davidmoremad/awspice)




Example
-------

If you want to get instances that doesn't match with the naming convention, you just need to run these lines:

.. code-block:: python

    import durex

    durex = durex.Durex('aws_account')

    instances = durex.ec2.ec2_instances_naming_convention()
