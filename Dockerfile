FROM python:3
RUN git clone https://github.com/um-computacion-tm/parcial-2-2022-temPLAY333
WORKDIR /parcial-2-2022-temPLAY333
CMD ["python3" ,"-m",  "unittest"]