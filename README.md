# TodoList
1. 할 일 목록
2. 할 일 등록
3. 할 일 삭제
4. 할 일 상태관리
        1) 대기(WAIT) 상태 목록 조회
            * 완료 숨김
            * 시작 버튼 → 진행(ING)
        2) 진행(ING) 상태 목록 조회
            *완료 출력
            *완료 체크 → 완료(DONE)
5. 완료 목록
    * 상태가 완료(DONE)인 목록 조회





완료목록 html
    <h3>대기 목록</h3>
            <table class="table table-bordered text-center align-middle">
              <thead>
                <tr class="table-dark">
                  <th>✅</th>
                  <th class="text-start">할 일</th>
                  <th>✨</th>
                </tr>
              </thead>
              <tbody>
                {% for todo in wait_list %}
                <tr>
                  <td>
                    <form action="./ing" method="post">
                      {% csrf_token %}
                      <input type="hidden" name="no" value="{{ todo.no }}">
                      <button type="submit" class="btn btn-outline-primary">진행</button>
                    </form>
                  </td>
                  <td>
                    {{ todo.title }}
                  </td>
                  <td>
                    <form action="./delete" method="post">
                      {% csrf_token %}
                      <input type="hidden" name="no" value="{{ todo.no }}">
                      <button class="btn btn-danger">
                        <i class="bi bi-trash3"></i>
                      </button>
                    </form>
                  </td>
                </tr>
                {% empty %}
                <tr>
                  <td colspan="3" class="text-center text-muted">
                    조회된 데이터가 없습니다.
                  </td>
                </tr>
                {% endfor %}
              </tbody>
            </table>