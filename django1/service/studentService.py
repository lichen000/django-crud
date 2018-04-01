import logging
import traceback
import math
import mysql.connector
from entity.student import Student
from django1.config import db
from dto.page import PageResult


logger = logging.getLogger(__name__)

config = db.dbconfig

def get(id):
    sql = "SELECT * FROM t_student WHERE id = " + str(id)
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(sql)
        tempKey = cursor.column_names
        tempValue = cursor.fetchone()
    except Exception as e:
        logger.error(traceback.format_exc())
    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None:
            cnx.close()
    if tempValue is None:
        return None
    else:
        result = dict(zip(tempKey, tempValue))
        student = Student()
        for key in result:
            student[key] = result[key]
        return student

def getAll():
    sql = "SELECT * FROM t_student"
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(sql)
        tempKey = cursor.column_names
        tempValues = cursor.fetchall()
    except Exception as e:
        logger.error(traceback.format_exc())
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None:
            cnx.close()
    if (tempValues is None) or (len(tempValues) == 0):
        return tempValues
    else:
        students = []
        for tempValue in tempValues:
            result = dict(zip(tempKey, tempValue))
            student = Student()
            for key in result:
                student[key] = result[key]
            students.append(student)
        return students


def getAllPage(pageNo=0, pageSize=10):
    cnx = None
    cursor = None
    sql1 = "SELECT count(*) FROM t_student"
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(sql1)
        totalCounts = cursor.fetchone()[0]

        if totalCounts == 0:
            return PageResult(contents=[])
        else:
            beginIndex = pageSize * pageNo
            limit = pageSize
            sql2 = "SELECT * FROM t_student limit " + str(beginIndex) + " , " + str(limit)
            try:
                cursor.execute(sql2)
                tempKey = cursor.column_names
                tempValues = cursor.fetchall()
            except Exception as e1:
                logger.error(traceback.format_exc())
                return None
    except Exception as e2:
        logger.error(traceback.format_exc())
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None:
            cnx.close()

    if tempValues is None:
        return None
    else:
        students = []
        for tempValue in tempValues:
            result = dict(zip(tempKey, tempValue))
            student = Student()
            for key in result:
                student[key] = result[key]
            students.append(student)

    if totalCounts <= pageSize:
        totalPages = 1
    else:
        totalPages = math.ceil(totalCounts / pageSize)

    pageResult = PageResult(pageNo, pageSize, totalCounts, totalPages, students)

    return pageResult


def add(student):
    sql = "INSERT INTO t_student (note, name, number, age) values (%s, %s, %s, %s)"
    params = (student.note, student.name, student.number, student.age)
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(sql, params)
        cnx.commit()
        id = cursor.lastrowid
        entity = get(id)
        return entity
    except Exception as e:
        logger.error(traceback.format_exc())
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None:
            cnx.close()

def update(id,updatedParams,student):
    sql = " UPDATE t_student SET note = %s, name = %s, number = %s, age = %s WHERE id = %s"
    params = (student.note, student.name, student.number, student.age, id)
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(sql, params)
        cnx.commit()
        entity = get(id)
        return entity
    except Exception as e:
        logger.error(traceback.format_exc())
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None:
            cnx.close()


def delete(id):
    sql = "DELETE FROM t_student WHERE id = " + str(id)
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        cursor.execute(sql)
        cnx.commit()  # 修改的语句要加一句这个
        return None
    except Exception as e:
        logger.error(traceback.format_exc())
        return None
    finally:
        if cursor is not None:
            cursor.close()
        if cnx is not None:
            cnx.close()
