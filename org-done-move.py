#!/usr/bin/python
# coding:UTF-8

import re

class OrgDoneMove:
    def check_head(self, line):
        regexp = re.compile("(^\*)")
        res = re.search(regexp, line)
        return res
    
    def check_status(self, line):
        regexp = re.compile("^\*([\*|\s])\s(.*?)[\s|$]")
        res = re.search(regexp, line)
        return res

    def move_task(self, movetasks):
        f = open("~/FinTask.org", "a+")
        for task in movetasks:
            f.write(task)
        f.close()

    def rewrite_org_file(self, remaintask):
        f = open("~/Todo.org", "w")
        for task in remaintask:
            f.write(task)
        f.close

    def read_file(self, path):
        movetask = []
        moveflag = 0

        remaintask = []
        remainflag = 0

        f = open(path, "r")
        lines = f.readlines()

        for line in lines:
            headres = self.check_head(line)
            if headres:
                res = self.check_status(line)
                if res:
                    if res.group(2) == "DONE":
                        movetask.append(line)
                        moveflag = 1
                        remainflag = 0
                    else:
                        remaintask.append(line)
                        moveflag = 0
                        remainflag = 1
                else:
                    remaintask.append(line)
                    moveflag = 0
                    remainflag = 0
            else:
                if moveflag:
                    movetask.append(line)
                elif remainflag:
                    remaintask.append(line)
                else:
                    pass

        self.move_task(movetask)
        self.rewrite_org_file(remaintask)

if __name__ == '__main__':
    orgdonemoveClass = OrgDoneMove()
    orgdonemoveClass.read_file("~/Todo.org")
