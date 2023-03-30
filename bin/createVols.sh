#!/bin/bash

dir="$(realpath .)/vols"

echo $dir

if [ ! -d $dir ]; then
  mkdir $dir;
fi

if [ ! -d "$dir/zk-data" ]; then
  mkdir "$dir/zk-data";
fi

if [ ! -d "$dir/zk-logs" ]; then
  mkdir "$dir/zk-logs";
fi

if [ ! -d "$dir/kafka-1-data" ]; then
  mkdir "$dir/kafka-1-data";
fi

if [ ! -d "$dir/kafka-2-data" ]; then
  mkdir "$dir/kafka-2-data";
fi