#!/bin/bash
seq -f "DDM%01g" 1 100| xargs mkdir
for((i = 1;i<101;i++))
do
	DDM="DDM"$i;
	cd $DDM
	touch time_till_now.txt
	cat>>time_till_now.txt<<EOF
nanoseconds since 1970-01-01 00:00:00 UTC:
EOF
	cur_time='<'`date +%s%N`'>'
	echo $cur_time >> time_till_now.txt
	cd ..
done
