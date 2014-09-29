Doobie
======

Hash on a pipe!

Ever needed to:

    tar cv dir1 dir2 | pigz| md5sum | ssh -q server 'cat - >backup.tar.gz'

Well, now you can:

    pip install doobie
    tar cv dir1 dir2 | pigz| python -m doobie -H md5 -o backup.md5 | ssh -q server 'cat - >backup.tar.gz'
    ssh server 'md5sum backup.tar.gz'

Supported hashes are:

 - sha1
 - sha224
 - sha384
 - sha256
 - sha512
 - md5
