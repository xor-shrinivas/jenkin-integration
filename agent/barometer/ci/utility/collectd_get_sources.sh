#!/bin/bash
# Copyright 2017 Intel┬áCorporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
source $DIR/package-list.sh

bash $DIR/check_git_repo.sh $COLLECTD_DIR $COLLECTD_REPO
if [[ $? != 0 ]]
then
	rm -rf $COLLECTD_DIR
	git clone $COLLECTD_REPO $COLLECTD_DIR
	cd $COLLECTD_DIR
else
	cd $COLLECTD_DIR
	git reset HEAD --hard
	git pull
fi
git checkout -f $COLLECTD_BRANCH
